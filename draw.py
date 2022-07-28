import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
blank[200:300,300:400]=255,255,255
cv.imshow("Green",blank)
w=blank.shape[1]//2
h=blank.shape[0]//2
cv.rectangle(blank,(0,0),(w,h),(0,255,0),thickness=cv.FILLED)
cv.imshow("Rectangle",blank)
cv.circle(blank,(w,h),50,(70,50),thickness=-1)
cv.imshow("Circle",blank)
#Writing text in a given image
cv.putText(blank,"Dont give up",(295,255),cv.FONT_HERSHEY_PLAIN,1.0,(255,238,123),thickness=3)
cv.imshow('Text in image ',blank)

cv.waitKey(0)