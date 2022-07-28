import cv2 as cv
img=cv.imread('Resources/Photos/cat_large.jpg')
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,width)

def rescaleFrame(frame,scale=0.45) :
    ##works for evry type of images and videos

    width=int (frame.shape[1]*scale)
    height = int(frame.shape[0] * scale)#shape[0]==height
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)


capture=cv.VideoCapture('Resources/Videos/dog.mp4')#use 0 if you have webcam
resized_img=rescaleFrame(img)
#changeRes(20,20)
cv.imshow("My image",img)
cv.imshow("My resized image",resized_img)
while True:
    isTrue, frame = capture.read()
    frame_resized=rescaleFrame(frame,scale=0.6)

    cv.imshow('Video',frame)
    cv.imshow("video2",frame_resized)
    if cv.waitKey(20) & 0xFF==ord('q'):
        break
        

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)