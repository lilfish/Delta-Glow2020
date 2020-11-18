# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2

capture = cv2.VideoCapture(0)
bodyCascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

def distance_to_camera(image, knownWidth, focalLength, perWidth):
    # compute and return the distance from the maker to the camera
    return (knownWidth * focalLength) / perWidth

def body_tracking():
    while True:
        # Read the frame
        _, img = capture
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = bodyCascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Display
        cv2.imshow('img', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    # Release the VideoCapture object
    capture.release()

def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh

def draw_detections(img, rects, thickness=1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15 * w), int(0.05 * h)
        cv2.rectangle(img, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), thickness)


body_tracking()

# bodyDetector = bodyCascade
# count = 0
# while (True):
#     # # Our operations on the frame come here
#     # KNOWN_DISTANCE = 30
#     # KNOWN_WIDTH = 30
#     # marker = find_marker(frame)
#     # focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
#     # centimetre = distance_to_camera(frame,KNOWN_WIDTH, focalLength, marker[1][0])
#     # # draw a bounding box around the image and display it
#     # box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
#     # box = np.int0(box)
#     # cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
#     # cv2.putText(
#     #     frame,
#     #     "%.2fft" % (centimetre / 12),
#     #     (frame.shape[1] - 200, frame.shape[0] - 20),
#     #     cv2.FONT_HERSHEY_SIMPLEX,
#     #     2.0,
#     #     (0, 255, 0),
#     #     3,
#     # )
#     # # Display the resulting frame
#     # cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# capture.release()
# cv2.destroyAllWindows()
#
# def find_marker(image):
#     # convert the image to grayscale, blur it, and detect edges
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     gray = cv2.GaussianBlur(gray, (5, 5), 0)
#     edged = cv2.Canny(gray, 35, 125)
#     # find the contours in the edged image and keep the largest one
#     cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     c = max(cnts, key=cv2.contourArea)
#     # compute the bounding box of the of the paper region and return it
#     return cv2.minAreaRect(c)