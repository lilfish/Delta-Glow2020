# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2

capture = cv2.VideoCapture(0)
upperBodyCascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
fullBodyCascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')


def upperBodyTrack():

    count = 0

    while True:
        img = capture.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        body = upperBodyCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in body:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Upper Body', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def fullBodyTrack():
    count = 0

    while True:
        img = capture.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        body = fullBodyCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in body:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Full Body', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




