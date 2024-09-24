import cv2
import numpy as np

#wear red shirt 
videocapture = cv2.VideoCapture(0)
frames = 0

for i in range(60):
    video, frames = videocapture.read()

inverted = np.flip(frames, axis= 1)

while True:
    print("inverted")
    video, frames = videocapture.read()
    if video == False:
        break
    invertion = np.flip(frames, axis= 1)
    saturation = cv2.cvtColor(invertion, cv2.COLOR_BGR2HSV) #convert to HSV
    lowerrange = np.array([100, 40, 40])
    upperrange = np.array([100,255,255])
    mask = cv2.inRange(saturation, lowerrange, upperrange)
    lowerrange2 = np.array([155,40,40])
    upperrange2 = np.array([180,255,255])
    mask2 = cv2.inRange(saturation, lowerrange2, upperrange2)
    combine = mask + mask2

    refine = cv2.morphologyEx(combine, cv2.MORPH_OPEN, np.ones((3,3),dtype = int), iterations = 2 )
    mask1 = cv2.dilate(refine, np.ones((3,3),dtype = int), iterations = 2)
    mask2 = cv2.bitwise_not(mask1) #opposite
    red = cv2.bitwise_and(inverted, inverted, mask = mask1) #inverted means that it is the first frame that occurs when you start the code
    nored = cv2.bitwise_and(invertion, invertion, mask = mask2)
    combine2 = cv2.addWeighted(red, 1, nored, 1, 0)
    cv2.imshow("display", combine2)
    if cv2.waitKey(10) == 32:
        break 

