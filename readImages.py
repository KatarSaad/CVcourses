import cv2 as cv
##img=cv.imread('Resources/Photos/cat_large.jpg')
##cv.imshow("cat",img)
##cv.waitKey(0)#importing images and showing them

#### Reading Videos


capture=cv.VideoCapture('Resources/Videos/dog.mp4')#use 0 if you have webcam
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)