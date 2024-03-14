import face_recognition
import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # default camera of laptop is 0

KK_img = face_recognition.load_image_file('face-recognition\img_train\KK')
KK_face_encode = face_recognition.face_encodings(KK_img)[0]

KK_img = face_recognition.load_image_file('face-recognition\img_train\KK')
KK_face_encode = face_recognition.face_encodings(KK_img)[0]

KK_img = face_recognition.load_image_file('face-recognition\img_train\KK')
KK_face_encode = face_recognition.face_encodings(KK_img)[0]

while True:
    ret, frame = cap.read()
    if ret:  # if cam read(True) from cap variable, Camera is opened
        cv2.imshow("Camera", frame)
        # if user pess q from keyboard camera is turn off
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Program has stopped by user.")
            break
    else:
        break
