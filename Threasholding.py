import cv2 as cv
img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow("Catis",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
#Simple Treashold

threashold,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow("Threashold",thresh)

threashold,thresh_inv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV )
   #########Returns pixels that are  lesser than 100 in white(255)

cv.imshow("Threashold",thresh_inv)
#Now adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow("adaptive",adaptive_thresh)





cv.waitKey(0)