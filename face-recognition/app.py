from flask import Flask, render_template, request
import cv2
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    camera = cv2.VideoCapture(0)  # เปิดกล้อง
    return_value, image = camera.read()  # อ่านภาพจากกล้อง
    camera.release()  # ปิดกล้อง
    if return_value:
        cv2.imwrite('static/captured_image.jpg', image)  # เก็บภาพลงในโฟลเดอร์ static
        return 'Capture successful!'
    else:
        return 'Failed to capture image!'

if __name__ == '__main__':
    app.run(debug=True)
