import cv2 as cv
import numpy as np

img=cv.imread('Resources/Photos/park.jpg')
cv.imshow("Catis",img)
import numpy as np

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Laplacian

lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))

#Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)

sobely=cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow("Sobely",sobely)
cv.imshow("Sobelx",sobelx)
combined=cv.bitwise_or(sobely,sobelx)
cv.imshow("Combined",combined)
##Canny multi process algorithm
canny=cv.Canny(gray,150,175)
cv.imshow("Canny",canny)




cv.imshow("Laplacian",lap)







cv.waitKey(0)