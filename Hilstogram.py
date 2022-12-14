import numpy as    np
import cv2 as  cv
import matplotlib.pyplot as plt

img=cv.imread("Resources/Photos/cats.jpg")
blank= np.zeros(img.shape[:2],dtype="uint8")
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)


cv.imshow('Cats',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
###Gray histogram
masked=cv.bitwise_and(img,img,mask=mask )

#gray_histo=cv.calcHist([gray],[0],mask,[256],[0,256])
'''plt.figure()
plt.title("Gray scale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_histo)
plt.xlim([0,256])
plt.show()
'''
###Colored Histogram
bgr_histo=cv.calcHist([img],[0],mask,[256],[0,256])
colors=('b','g','r')
plt.figure()
plt.title("Colored Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.imshow("Mask",mask)


cv.waitKey(0)

