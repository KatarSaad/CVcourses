import cv2 as cv
import numpy as np


img=cv.imread('Resources/Photos/cats.jpg')
blank=np.zeros(img.shape,dtype="uint8")

cv.imshow("Cats",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray sclae cats",gray)
cv.waitKey(0)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

canny=cv.Canny(blur,125,175)
cv.imshow("Canny Cats ",canny)
ret,threshold=cv.threshold(gray,125,255,cv.THRESH_BINARY)###Binarry form Black oe White
cv.imshow("Threachold",threshold)###Activate and disactivate Pixels when reaching certain value or gray in gray scale pixel


contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("Contour in new Blank image",blank)
print(f'{len(contours)} contours found')


cv.waitKey(0)


