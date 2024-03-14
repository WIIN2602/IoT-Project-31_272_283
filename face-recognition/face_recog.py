import face_recognition
import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Program has stopped by user.")
            break
    else:
        break
