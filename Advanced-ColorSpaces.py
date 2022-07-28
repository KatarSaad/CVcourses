import cv2 as cv
import matplotlib.pyplot as plt


img=cv.imread("Resources/Photos/park.jpg")
#plt.imshow(img)
#plt.show()

cv.imshow('Bosston',img)

#gray sclae image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#hsv color
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)
#Lab format
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)####

###mathplot lib does not know BGR IMAGES

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)

#plt.imshow(rgb)
#plt.show()
#cv.waitKey(0)'''

    ###### We can convert images to BGR ////But we cant directly convert GRay scale into HSV Directly ...

#LAB to BGR
bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("Lab-->BGR",bgr)
cv.waitKey(0)

