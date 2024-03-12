import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'image/CLASSNAMES'
images = []
ClassNames = []
checkList = os.listdir(path)
print(checkList)

for cls in checkList :
    current_img = cv2.imread(f'{path}/{cls}')
    images.append(current_img)
    ClassNames.append(os.path.splitext(cls)[0])
print(ClassNames)

def findEncodings(images):
    encodinglist = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        if len(encode) > 0:  # Ensuring there's at least one face detected
            encodinglist.append(encode[0])  # Take only the first face encoding
    return encodinglist
def markAttendance(name) :
    with open('Attendance.csv','r+') as f:
        DataList = f.readlines()
        nameList = []
        for line in DataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            DtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{DtString}')

encodeListKnown = findEncodings(images)
print('Encode Complete')

cap = cv2.VideoCapture(1)
while True:
    success, img = cap.read()
    image_small = cv2.resize(img,(0,0),None,0.25,0.25)
    image_small = cv2.cvtColor(image_small,cv2.COLOR_BGR2RGB)

    faceCurrentFrame = face_recognition.face_locations(image_small)
    encodeCurrentFrame = face_recognition.face_encodings(image_small,faceCurrentFrame)

    for encodeFace,faceLoc in zip(encodeCurrentFrame,faceCurrentFrame):
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)
        if len(faceDis) == len(checkList):  # Ensure face distance length matches checkList length
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                name = ClassNames[matchIndex].upper()
                print(name)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y1-35), (x2, y2-35), (0, 255, 0), 3, cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)
    cv2.imshow('webcam',img)
    cv2.waitKey(1)