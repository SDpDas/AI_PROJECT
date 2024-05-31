#lane line video detection

import cv2
import numpy as np

video = cv2.VideoCapture("test_video cropped.mp4")

roi = np.array([(0, 720), (1280, 720), (750, 450), (550, 450)])
while True:
    ret, orig_frame = video.read() #reading frames from the video
    if not ret:
        video = cv2.VideoCapture("test.mp4")
        continue #Looping the video

    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0) #Applies Gaussian Blur
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converts frame to show yellow lines
    
    low_yellow = np.array([18, 94, 140]) #lower threshold for yellow
    up_yellow = np.array([48, 255, 255]) #higher threshold for yellow
    mask1 = cv2.inRange(hsv, low_yellow, up_yellow) #creates binary mask
    

    low_white = np.array([0, 0, 200]) #lower threshold for white
    up_white = np.array([180, 25, 255]) #higher threshold for white
    mask2 = cv2.inRange(hsv, low_white, up_white) #creates binary mask
    
    combined_mask = cv2.bitwise_or(mask1, mask2)
    
    edges = cv2.Canny(combined_mask, 75, 150) #Canny edge detection

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
    if lines is not None: #to remove error if no line present
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)


    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)
    key = cv2.waitKey(25)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()