import numpy as    np
import cv2 as  cv
img=cv.imread("Resources/Photos/cats.jpg")
cv.imshow('Cats',img)
blank= np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("Blank image",blank)
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked",masked)
cv.waitKey(0)
###Create a Mask like  ip @ that activate when blank(mask) pixels are white
###the mask needs to be at the same size of the curent image
