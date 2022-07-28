import cv2 as cv
import numpy as np
img=cv.imread("Resources/Photos/park.jpg")
cv.imshow("park",img)

#IMAGE TRANSFORMATION

    #TRANSLATION

def translation (img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dim=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dim)

translated=translation(img,-100,100)
#cv.imshow("Translated",translated)

    #ROTATION

def rotation (img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dim=(width,height)
    return cv.warpAffine(img,rotMat,dim)
rotated=rotation(img,45)
#cv.imshow("Rotated Image",rotated)

       #RESIZNG

resized =cv.resize(img,(300,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resize",resized)

       #FLIPING

flp=cv.flip(img,1)
cv.imshow("flip",flp)

      #Croping
croped=img[19:200,300:400]
#cv.imshow("croped",croped)



cv.waitKey(0)
