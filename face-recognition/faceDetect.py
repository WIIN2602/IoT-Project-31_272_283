import cv2
import cv2 as cv
import numpy as np
import face_recognition
import os

path = 'image/CLASSNAMES'
images = []
ClassNames = []
List_Classname = os.listdir(path)
print(List_Classname)

for cls in List_Classname :
    current_img = cv2.imread(f'{path}/{cls}')
    images.append(current_img)
    ClassNames.append(os.path.splitext(cls)[0])
print(ClassNames)

def findEncodings(images):
    encodinglist = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        encodinglist.append(encode)
    return encodinglist

encodeListKnown = findEncodings(images)
print('Encode Complete')
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    faceCurrentFrame = face_recognition.face_locations(imgS)
    encodeCurrentFrame = face_recognition.face_encodings(imgS,faceCurrentFrame)

    for encodeFace,faceLoc in zip(encodeCurrentFrame,faceCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)


# img = face_recognition.load_image_file('image/kk2.jpg')
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# img2 = face_recognition.load_image_file('image/kk3.jpg')
# img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)