# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2


capture = cv2.VideoCapture(0)
bodyCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)
    # find the contours in the edged image and keep the largest one
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    # compute the bounding box of the of the paper region and return it
    return cv2.minAreaRect(c)


def distance_to_camera(image,knownWidth, focalLength, perWidth):
    # compute and return the distance from the maker to the camera
    return (knownWidth * focalLength) / perWidth


bodyDetector = bodyCascade
count = 0
while(True):
    # Capture frame-by-frame
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    people = bodyDetector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in people:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        gray = cv2.resize(gray[y:y + h, x:x + w], (128, 128), interpolation=cv2.INTER_AREA)

    # Our operations on the frame come here
    KNOWN_DISTANCE = 30
    KNOWN_WIDTH = 30
    marker = find_marker(frame)
    focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
    centimetre = distance_to_camera(frame,KNOWN_WIDTH, focalLength, marker[1][0])
    # draw a bounding box around the image and display it
    box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
    box = np.int0(box)
    cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
    cv2.putText(
        frame,
        "%.2fft" % (centimetre / 12),
        (frame.shape[1] - 200, frame.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        2.0,
        (0, 255, 0),
        3,
    )
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()



