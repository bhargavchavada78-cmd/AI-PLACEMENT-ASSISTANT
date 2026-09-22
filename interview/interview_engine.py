from .questions import get_questions
from .nlp_analyzer import analyze_answer
from .speech_analyzer import (
    count_words,
    count_filler_words,
    calculate_wpm,
    speech_score
)

from .confidence import (
    calculate_confidence,
    confidence_label,
    confidence_feedback
)


class InterviewEngine:

    def __init__(self, role):

        self.role = role

        self.questions = (
            get_questions(role)
        )

        self.current_index = 0

        self.results = []


    def current_question(self):

        if (
            self.current_index
            >= len(self.questions)
        ):

            return None

        return self.questions[
            self.current_index
        ]


    def submit_answer(
        self,
        answer,
        duration_seconds=60,
        video_score=100
    ):

        question = (
            self.current_question()
        )

        if question is None:

            return None


        # NLP analysis

        nlp_result = analyze_answer(
            answer,
            question
        )


        # Speech analysis

        word_count = count_words(
            answer
        )

        filler_count, fillers = (
            count_filler_words(
                answer
            )
        )

        wpm = calculate_wpm(
            word_count,
            duration_seconds
        )

        speech_result = speech_score(
            wpm,
            filler_count
        )


        # Communication confidence indicator

        confidence = calculate_confidence(
            nlp_result["score"],
            speech_result,
            video_score
        )


        result = {

            "question":
                question["question"],

            "answer":
                answer,

            "answer_score":
                nlp_result["score"],

            "similarity":
                nlp_result["similarity"],

            "keyword_coverage":
                nlp_result[
                    "keyword_coverage"
                ],

            "found_keywords":
                nlp_result[
                    "found_keywords"
                ],

            "missing_keywords":
                nlp_result[
                    "missing_keywords"
                ],

            "word_count":
                word_count,

            "wpm":
                wpm,

            "filler_count":
                filler_count,

            "fillers":
                fillers,

            "speech_score":
                speech_result,

            "video_score":
                video_score,

            "confidence":
                confidence,

            "confidence_label":
                confidence_label(
                    confidence
                ),

            "confidence_feedback":
                confidence_feedback(
                    confidence
                ),

            "feedback":
                nlp_result[
                    "feedback"
                ]
        }


        self.results.append(
            result
        )

        self.current_index += 1

        return result


    def finished(self):

        return (
            self.current_index
            >= len(self.questions)
        )


    def final_report(self):

        if not self.results:

            return {

                "average_answer_score": 0,

                "average_confidence": 0,

                "questions": 0

            }


        answer_scores = [

            result["answer_score"]

            for result in self.results

        ]

        confidence_scores = [

            result["confidence"]

            for result in self.results

        ]


        return {

            "average_answer_score":
                round(
                    sum(answer_scores)
                    /
                    len(answer_scores),
                    2
                ),

            "average_confidence":
                round(
                    sum(confidence_scores)
                    /
                    len(confidence_scores),
                    2
                ),

            "questions":
                len(self.results),

            "results":
                self.results
        }