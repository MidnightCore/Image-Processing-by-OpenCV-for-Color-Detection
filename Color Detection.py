#color detection of yellow and green color in image

#necessary libraries

import cv2  
import numpy as np

green = np.uint8([[[71, 213, 144]]])  #green color
hsvGreen = cv2.cvtColor(green, cv2.COLOR_BGR2HSV) #hsv value of green color 
print(hsvGreen)
lowerLimit = hsvGreen[0][0][0] - 12, 100, 100  # range of green color lower limit and upper limit
upperLimit = hsvGreen[0][0][0] + 10, 255, 255
print(upperLimit)
print(lowerLimit)


gy = np.uint8([[[58, 179, 191]]])  #gy color
hsvgy = cv2.cvtColor(gy, cv2.COLOR_BGR2HSV) #hsv value of gy color
print(hsvgy)
lLimit = hsvgy[0][0][0] - 1, 100, 100  # range of gy color lower limit and upper limit
uLimit = hsvgy[0][0][0] + 5, 255, 255
print(uLimit)
print(lLimit)


yellow = np.uint8([[[187, 221, 239]]]) #yellow color
hsvyellow = cv2.cvtColor(yellow, cv2.COLOR_BGR2HSV) #hsv value of yellow color
print(hsvyellow)
lower = hsvyellow[0][0][0] - 10, 100, 100 # range of yellow color lower limit and upper limit
upper = hsvyellow[0][0][0] + 5, 255, 255
print(upper)
print(lower)


#image = cv2.imread(r'mango_test.jpg') #load your image
image = cv2.imread(r'allmango1.png') #load your image
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #convert the image into hsv


lg = np.array(lowerLimit) #range of green color
ug = np.array(upperLimit)
green_mask = cv2.inRange(hsv, lg, ug) #green masked image
cv2.imshow('green - Raw', green_mask) #show the image


ll = np.array(lLimit) #range of gy color
ul = np.array(uLimit)
green_mask = cv2.inRange(hsv, ll, ul) #gy masked image
cv2.imshow('green_yellow - Near Ripe', green_mask) #show the image


lr = np.array(lower) #range of yellow color
ur = np.array(upper)
yellow_mask = cv2.inRange(hsv, lr, ur) #yellow masked image
cv2.imshow('yellow - Ripe', yellow_mask)  #show the image


cv2.waitKey(0)
cv2.destroyAllWindows()