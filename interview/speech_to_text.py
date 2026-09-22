from faster_whisper import WhisperModel


class SpeechToText:

    def __init__(self):

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )


    def transcribe(self, audio_file):

        segments, info = self.model.transcribe(
            audio_file
        )

        text = ""

        for segment in segments:

            text += segment.text + " "

        return text.strip()