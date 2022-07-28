import cv2 as cv
import numpy as np
img=cv.imread("Resources/Photos/park.jpg")

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("park",img)
b,g,r=cv.split(img)
blue =cv.merge([b,blank,blank])

green =cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow("Red",red)
cv.imshow("Blue",blue)
cv.imshow('Green',green)

cv.imshow("blue",b)
cv.imshow("red",r)
cv.imshow("green",g)
print(img.shape)
print (r.shape)
print(b.shape)
print(g.shape)
###Now let us merge this r,g,b color images
merged=cv.merge([b,g,r])
cv.imshow("mergedImages",merged)

cv.waitKey(0)