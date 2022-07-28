import cv2 as cv
import numpy as np
people =["Ben Afflek","Elton John","Jerry","Madonna","Mindy Kaling"]

har_cascade=cv.CascadeClassifier("haar_face.xml")
features=np.load("features.npy",allow_pickle=True)
labels=np.load("labels.npy")
face_rec=cv.face.LBPHFaceRecognizer_create()
face_rec.read('face_trained.yml')
img=cv.imread("C:/Users/Saad/PycharmProjects/OpenCvCourse/Resources/Faces/train/Elton John/5.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Person",gray)

#detecting faces
face_rect=har_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4 )
for (x,y,w,h) in face_rect:
    faces_roi=gray[y:y+h,x:x+h]
    label,confidence=face_rec.predict(faces_roi)
    print(f'label={people[label]} with a confidance of {confidence}')
    cv.putText(img,str(people[label]),(20,20),cv.FONT_ITALIC,1.0,(0,255,0))
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    cv.imshow("img face detected    ",img)
cv.waitKey(0)

