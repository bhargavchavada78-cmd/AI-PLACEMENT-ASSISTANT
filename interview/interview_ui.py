import os
import time
import streamlit as st

from .questions import QUESTIONS
from .interview_engine import InterviewEngine
from .speech_to_text import SpeechToText


 
# INITIALIZE SESSION


def initialize():

    if "interview_engine" not in st.session_state:
        st.session_state.interview_engine = None

    if "interview_started" not in st.session_state:
        st.session_state.interview_started = False

    if "answer_start_time" not in st.session_state:
        st.session_state.answer_start_time = None

    if "question_audio" not in st.session_state:
        st.session_state.question_audio = {}

    if "speech_model" not in st.session_state:
        st.session_state.speech_model = None



# START INTERVIEW


def show_interview():

    initialize()

    st.title("🎤 Live AI Interview Assistant")

    st.subheader("Select Interview Domain")

    
    role = st.selectbox(
        "Choose Domain",
        list(QUESTIONS.keys()),
        key="interview_role"
    )
    st.info(f"Selected Domain: {role}")

    if role is None:

        st.warning(
            "Please select an interview domain from the sidebar."
        )

        return

    

    if not st.session_state.interview_started:

        st.subheader(
            f"🎯 Interview Domain: {role}"
        )

        

        

        if st.button(
            "🚀 Start Interview",
            use_container_width=True
        ):

            st.session_state.interview_engine = (
                InterviewEngine(role)
            )

            st.session_state.interview_started = True

            st.session_state.answer_start_time = (
                time.time()
            )

            st.session_state.question_audio = {}

            # Load Whisper only when interview starts
            with st.spinner(
                "Loading speech recognition model..."
            ):

                st.session_state.speech_model = (
                    SpeechToText()
                )

            st.rerun()

        return

    # =====================================================
    # GET ENGINE
    # =====================================================

    engine = (
        st.session_state.interview_engine
    )

    # Safety check

    if engine is None:

        st.session_state.interview_started = False

        st.rerun()

        return

    # =====================================================
    # FINAL REPORT
    # =====================================================

    if engine.finished():

        report = (
            engine.final_report()
        )

        st.success(
            "🎉 Interview Completed!"
        )

        # -------------------------------------------------
        # SUMMARY
        # -------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Average Answer Score",
                f"{report['average_answer_score']}%"
            )

        with col2:

            st.metric(
                "Average Confidence",
                f"{report['average_confidence']}/100"
            )

        with col3:

            st.metric(
                "Questions",
                report["questions"]
            )

        st.divider()

        st.subheader(
            "📊 Interview Report"
        )

        # -------------------------------------------------
        # QUESTION RESULTS
        # -------------------------------------------------

        for index, result in enumerate(
            report["results"],
            start=1
        ):

            with st.expander(
                f"Question {index}"
            ):

                st.markdown(
                    f"### ❓ {result['question']}"
                )

                st.markdown(
                    "### 📝 Transcribed Answer"
                )

                st.write(
                    result["answer"]
                )

                st.divider()

                # -----------------------------------------
                # SCORE
                # -----------------------------------------

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Answer Score",
                        f"{result['answer_score']}%"
                    )

                with col2:

                    st.metric(
                        "NLP Similarity",
                        f"{result['similarity']}%"
                    )

                with col3:

                    st.metric(
                        "Confidence",
                        f"{result['confidence']}/100"
                    )

                # -----------------------------------------
                # SPEECH ANALYSIS
                # -----------------------------------------

                st.markdown(
                    "### 🎤 Speech Analysis"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Words",
                        result["word_count"]
                    )

                with col2:

                    st.metric(
                        "WPM",
                        result["wpm"]
                    )

                with col3:

                    st.metric(
                        "Filler Words",
                        result["filler_count"]
                    )

                # -----------------------------------------
                # KEYWORDS
                # -----------------------------------------

                st.markdown(
                    "### 🔑 Keyword Analysis"
                )

                if result["found_keywords"]:

                    st.success(
                        "Found: "
                        +
                        ", ".join(
                            result["found_keywords"]
                        )
                    )

                if result["missing_keywords"]:

                    st.warning(
                        "Missing concepts: "
                        +
                        ", ".join(
                            result["missing_keywords"]
                        )
                    )

                # -----------------------------------------
                # FEEDBACK
                # -----------------------------------------

                st.markdown(
                    "### 💡 Answer Feedback"
                )

                st.info(
                    result["feedback"]
                )

                st.markdown(
                    "### 🗣️ Communication Feedback"
                )

                st.caption(
                    result[
                        "confidence_feedback"
                    ]
                )

        st.divider()

        # -------------------------------------------------
        # NEW INTERVIEW
        # -------------------------------------------------

        if st.button(
            "🔄 Start New Interview",
            use_container_width=True
        ):

            st.session_state.interview_engine = None

            st.session_state.interview_started = False

            st.session_state.answer_start_time = None

            st.session_state.question_audio = {}

            st.session_state.speech_model = None

            st.rerun()

        return

    # =====================================================
    # CURRENT QUESTION
    # =====================================================

    question = (
        engine.current_question()
    )

    if question is None:

        st.rerun()

        return

    question_index = (
        engine.current_index
    )

    # =====================================================
    # PROGRESS
    # =====================================================

    total_questions = (
        len(engine.questions)
    )

    current_question_number = (
        question_index + 1
    )

    progress = (
        current_question_number
        /
        total_questions
    )

    st.progress(
        progress
    )

    st.subheader(
        f"Question {current_question_number} "
        f"/ {total_questions}"
    )

    # =====================================================
    # QUESTION
    # =====================================================

    st.markdown(
        f"## ❓ {question['question']}"
    )

    st.divider()

    # =====================================================
    # LIVE DASHBOARD
    # =====================================================

    left, right = st.columns(
        [1.2, 1]
    )

    # -----------------------------------------------------
    # CAMERA
    # -----------------------------------------------------

    with left:

        st.subheader(
            "🎥 Camera"
        )

        camera_image = st.camera_input(
            "Camera",
            label_visibility="collapsed",
            key=f"camera_{question_index}"
        )

        if camera_image:

            st.image(
                camera_image,
                use_container_width=True
            )

            st.success(
                "Camera ready"
            )

        else:

            st.info(
                "Enable camera when requested "
                "by your browser."
            )

    # -----------------------------------------------------
    # LIVE STATUS
    # -----------------------------------------------------

    with right:

        st.subheader(
            "📊 Live Indicators"
        )

        st.success(
            "🎥 Camera: Ready"
        )

        st.success(
            "🎤 Microphone: Ready"
        )

        st.success(
            "🧠 NLP: Ready"
        )

        

        

    st.divider()

    # =====================================================
    # ANSWER TIMER
    # =====================================================

    if st.session_state.answer_start_time is None:

        st.session_state.answer_start_time = (
            time.time()
        )

    # =====================================================
    # AUDIO RECORDING
    # =====================================================

    st.subheader(
        "🎤 Record Your Answer"
    )

    st.write(
        "Speak your answer using the microphone."
    )

    audio = st.audio_input(
        "🎙️ Start Recording",
        sample_rate=16000,
        key=f"audio_question_{question_index}"
    )

    # =====================================================
    # AUDIO RECEIVED
    # =====================================================

    if audio:

        st.session_state.question_audio[
            question_index
        ] = audio

        st.success(
            "✅ Audio recorded successfully."
        )

        st.audio(
            audio
        )

        st.caption(
            "Your answer is ready for "
            "speech-to-text analysis."
        )

    else:

        st.info(
            "🎤 Record your answer before submitting."
        )

    st.divider()

    # =====================================================
    # SUBMIT ANSWER
    # =====================================================

    if st.button(
        "✅ Submit Answer",
        use_container_width=True
    ):

        # -----------------------------------------------
        # CHECK AUDIO
        # -----------------------------------------------

        if audio is None:

            st.error(
                "Please record your answer first."
            )

            st.stop()

        # -----------------------------------------------
        # CALCULATE DURATION
        # -----------------------------------------------

        start_time = (
            st.session_state.answer_start_time
        )

        duration = (
            time.time() - start_time
            if start_time
            else 60
        )

        # Prevent zero duration

        if duration <= 0:

            duration = 1

        # -----------------------------------------------
        # SAVE AUDIO
        # -----------------------------------------------

        recording_folder = (
            "interview_recordings"
        )

        os.makedirs(
            recording_folder,
            exist_ok=True
        )

        audio_path = os.path.join(
            recording_folder,
            f"question_{question_index + 1}.wav"
        )

        with open(
            audio_path,
            "wb"
        ) as file:

            file.write(
                audio.getbuffer()
            )

        # -----------------------------------------------
        # SPEECH TO TEXT
        # -----------------------------------------------

        with st.spinner(
            "🎧 Converting speech to text..."
        ):

            try:

                speech_model = (
                    st.session_state.speech_model
                )

                if speech_model is None:

                    speech_model = (
                        SpeechToText()
                    )

                    st.session_state.speech_model = (
                        speech_model
                    )

                answer = speech_model.transcribe(
                    audio_path
                )

            except Exception as e:

                st.error(
                    "Speech-to-text failed."
                )

                st.exception(e)

                st.stop()

        # -----------------------------------------------
        # CHECK TRANSCRIPT
        # -----------------------------------------------

        if not answer:

            st.error(
                "No speech was detected in your recording. "
                "Please record your answer again."
            )

            st.stop()

        answer = answer.strip()

        # -----------------------------------------------
        # SHOW TRANSCRIPT
        # -----------------------------------------------

        st.subheader(
            "📝 Your Answer"
        )

        st.write(
            answer
        )

        # -----------------------------------------------
        # ANALYZE ANSWER
        # -----------------------------------------------

        with st.spinner(
            "🧠 Analyzing your answer..."
        ):

            try:

                result = engine.submit_answer(
                    answer=answer,
                    duration_seconds=duration,
                    video_score=100
                )

            except Exception as e:

                st.error(
                    "Answer analysis failed."
                )

                st.exception(e)

                st.stop()

        # =================================================
        # RESULT
        # =================================================

        st.success(
            "✅ Answer analyzed successfully!"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Answer Score",
                f"{result['answer_score']}%"
            )

        with col2:

            st.metric(
                "NLP Similarity",
                f"{result['similarity']}%"
            )

        with col3:

            st.metric(
                "Confidence",
                f"{result['confidence']}/100"
            )

        st.info(
            result["confidence_feedback"]
        )

        # =================================================
        # IMPORTANT
        # =================================================
        #
        # InterviewEngine.submit_answer()
        # already executes:
        #
        # self.current_index += 1
        #
        # Therefore we DO NOT call:
        #
        # engine.next_question()
        #
        # =================================================

        st.session_state.answer_start_time = None

        # Move automatically to next question
        st.rerun()