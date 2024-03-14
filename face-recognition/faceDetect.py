import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import docopt
from sklearn import svm


def fac_recognize(dir, test):
    encodings = []
    names = []
    if dir[-1] != '/':
        dir += '/'
    train_dir = os.listdir(dir)

    # Loop through each person in the training directory
