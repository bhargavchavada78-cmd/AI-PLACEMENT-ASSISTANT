import cv2


class LiveCamera:

    def __init__(self):

        self.camera = cv2.VideoCapture(0)

        self.face_detector = (
            cv2.CascadeClassifier(
                cv2.data.haarcascades +
                "haarcascade_frontalface_default.xml"
            )
        )


    def read_frame(self):

        success, frame = (
            self.camera.read()
        )

        if not success:

            return None, 0

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        faces = (
            self.face_detector.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5
            )
        )

        for (
            x,
            y,
            w,
            h
        ) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        face_count = len(faces)

        return frame, face_count


    def release(self):

        self.camera.release()