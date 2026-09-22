import re


FILLER_WORDS = [
    "um",
    "uh",
    "hmm",
    "like",
    "actually",
    "basically",
    "you know",
    "sort of",
    "kind of"
]


def count_words(text):

    words = text.split()

    return len(words)


def count_filler_words(text):

    text = text.lower()

    total = 0

    detected = []

    for filler in FILLER_WORDS:

        pattern = r"\b" + re.escape(filler) + r"\b"

        count = len(
            re.findall(
                pattern,
                text
            )
        )

        if count > 0:

            total += count

            detected.append(
                filler
            )

    return total, detected


def calculate_wpm(
    word_count,
    duration_seconds
):

    if duration_seconds <= 0:

        return 0

    minutes = duration_seconds / 60

    return round(
        word_count / minutes,
        2
    )


def speech_score(
    wpm,
    filler_count
):

    # Comfortable conversational range is treated
    # as an indicator, not a psychological measurement.

    if 100 <= wpm <= 160:

        speed_score = 100

    elif 80 <= wpm < 100:

        speed_score = 80

    elif 160 < wpm <= 180:

        speed_score = 80

    else:

        speed_score = 60


    if filler_count == 0:

        filler_score = 100

    elif filler_count <= 3:

        filler_score = 90

    elif filler_count <= 6:

        filler_score = 75

    else:

        filler_score = 60


    score = (
        speed_score * 0.6
        +
        filler_score * 0.4
    )

    return round(
        score,
        2
    )