import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def calculate_similarity(
    candidate_answer,
    expected_answer
):

    candidate = clean_text(
        candidate_answer
    )

    expected = clean_text(
        expected_answer
    )

    if not candidate:

        return 0.0

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [
            candidate,
            expected
        ]
    )

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(
        similarity * 100,
        2
    )


def keyword_analysis(
    candidate_answer,
    keywords
):

    answer = clean_text(
        candidate_answer
    )

    found = []
    missing = []

    for keyword in keywords:

        keyword_clean = clean_text(
            keyword
        )

        if keyword_clean in answer:

            found.append(keyword)

        else:

            missing.append(keyword)

    if keywords:

        coverage = (
            len(found) /
            len(keywords)
        ) * 100

    else:

        coverage = 0

    return {

        "found": found,

        "missing": missing,

        "coverage": round(
            coverage,
            2
        )
    }


def calculate_answer_score(
    similarity,
    keyword_coverage
):

    score = (
        similarity * 0.6
        +
        keyword_coverage * 0.4
    )

    return round(
        score,
        2
    )


def generate_feedback(score):

    if score >= 80:

        return (
            "Strong technical answer. "
            "The response is relevant and "
            "covers important concepts."
        )

    elif score >= 60:

        return (
            "Good answer, but some important "
            "concepts could be explained better."
        )

    elif score >= 40:

        return (
            "The answer contains some relevant "
            "information, but needs more technical detail."
        )

    else:

        return (
            "The answer has low coverage of the "
            "expected concepts. Review the topic."
        )


def analyze_answer(
    candidate_answer,
    question
):

    similarity = calculate_similarity(
        candidate_answer,
        question["answer"]
    )

    keyword_result = keyword_analysis(
        candidate_answer,
        question["keywords"]
    )

    score = calculate_answer_score(
        similarity,
        keyword_result["coverage"]
    )

    return {

        "similarity": similarity,

        "keyword_coverage":
            keyword_result["coverage"],

        "found_keywords":
            keyword_result["found"],

        "missing_keywords":
            keyword_result["missing"],

        "score": score,

        "feedback":
            generate_feedback(score)
    }