import cv2
import pytesseract
from utils import preprocess

def capture_text():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()

    if not ret:
        return "Camera error."

    frame = cv2.resize(frame, None, fx=0.7, fy=0.7)
    processed = preprocess(frame)

    text = pytesseract.image_to_string(
        processed,
        lang="eng+tgl"
    )

    return text.strip()
