import cv2 as cv
img=cv.imread('Resources/Photos/cat.jpg')
img1=cv.imread('Resources/Photos/park.jpg')
#cv.imshow('Cat',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray Scale",gray)
gray1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
cv.imshow("boston1",img1)
#cv.imshow("boston2",gray1)

#Now let us Blur the image so we can remove some of the noise
blur=cv.GaussianBlur(img1,(7,7),cv.BORDER_DEFAULT)
#cv.imshow("Blur",blur)

#Now Let us edge detect
######### Using Canny PreBuilt edge detecting tool
canny=cv.Canny(img1,124,175)#threasholds
#cv.imshow("Canny edge detect",canny)
canny1 =cv.Canny(blur,123,174 )
#cv.imshow("Blured image ,edge detecting ",canny1)##see the deffirance ?

#Dialating images

dilated=cv.dilate(canny,(3,3),iterations=3)
#cv.imshow("Dialations",dilated)

#Erroded image

eroded =cv.erode(dilated,(3,3),iterations=3)
#cv.imshow("eroded",eroded)

       ####Resizing images
resized=cv.resize(img1,(500,500),interpolation=cv.INTER_CUBIC)#Cubic is better when enlarging images
cv.imshow('Resized',resized)
       ### Croping images

croped=img1[50:200,150:300]
cv.imshow('croped',croped)

cv.waitKey(0)