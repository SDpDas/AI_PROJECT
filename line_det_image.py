#code to detect lines in an image

import cv2
import numpy as np

def process_image(img):
    img = cv2.imread("lines2.png")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converts image to grayscale
    edges = cv2.Canny(gray, 75, 150) # Shows edges using canny edge detector

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=30, maxLineGap=100) # stores co-ordinates of the detected lines
    print(lines) # applies changes to line properties

    for line in lines:
        x1, y1, x2, y2 = line[0] # we take every line as array of an array and first initiliaze with 0
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3) #changing line properties


    cv2.imshow("Edges", edges) # shows image of detected lines
    cv2.imshow("Image", img) # shows original image
    cv2.waitKey(0)
    cv2.destroyAllWindows()

process_image("lines2.png")