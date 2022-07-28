import cv2 as cv
import numpy as np
img=cv.imread("Resources/Photos/cats.jpg")
cv.imshow("parrk",img)
###Avereging Blur  pixels of a kernell
averge=cv.blur(img,(3,3))
cv.imshow("Avg Blur",averge)
###Gausian Blur is averging giving weights
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian',gauss)

###Mean bluring /is finding median in a kernell
mean=cv.medianBlur(img,3)
cv.imshow("median",mean)###not meant for bigger kernells

###Bilateral Bluring: apply Bluring but keeps the edges
bilateral=cv.bilateralFilter(img,10,35,25)###sigmaSpace is how much far away pixels influance curent pixels ...
cv.imshow("Bilateral",bilateral)









cv.waitKey(0)

