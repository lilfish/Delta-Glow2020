# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2


capture = cv2.VideoCapture(0)


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


def distance_to_camera(knownWidth, focalLength, perWidth):
    # compute and return the distance from the maker to the camera
    return (knownWidth * focalLength) / perWidth


# initialize the known distance from the camera to the object, which
# in this case is 30 cm
KNOWN_DISTANCE = 30
# initialize the known object width, which in this case, the piece of
# paper is 35 cm wide
KNOWN_WIDTH = 30
# load the furst image that contains an object that is KNOWN TO BE 30cm
# from our camera, then find the paper marker in the image, and initialize
# the focal length
image = cv2.imread("images/30cm.jpg")
marker = find_marker(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH



while(True):
    # Capture frame-by-frame
    ret, frame = capture.read()

    # Our operations on the frame come here
    image = cv2.imread(frame)
    marker = find_marker(image)
    centimetre = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
    # draw a bounding box around the image and display it
    box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
    box = np.int0(box)
    cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
    cv2.putText(
        image,
        "%.2fft" % (centimetre / 12),
        (image.shape[1] - 200, image.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        2.0,
        (0, 255, 0),
        3,
    )
    # Display the resulting frame
    cv2.imshow('frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()



