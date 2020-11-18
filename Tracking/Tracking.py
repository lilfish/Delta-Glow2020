# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera

upperBodyCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')
fullBodyCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')




def upperBodyTrack():
    while True:
        ret, frame = capture.read()

        img = frame
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        body = upperBodyCascade.detectMultiScale(
            gray,
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in body:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('upper Body', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            capture.release()
            cv2.destroyAllWindows()

def fullBodyTrack():

    while True:
        ret, frame = capture.read()

        img = frame
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
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            capture.release()
            cv2.destroyAllWindows()





upperBodyTrack()