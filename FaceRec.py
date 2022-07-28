import cv2 as cv
import os
import numpy as np
img=cv.imread("")
people =["Ben Afflek","Elton John","Jerry","Madonna","Mindy Kaling"]
p=[]
DIR=r'C:/Users/Saad/PycharmProjects/OpenCvCourse/Resources/Faces/train'
haarCascade=cv.CascadeClassifier("haar_face.xml")

for i in os.listdir(r'C:/Users/Saad/PycharmProjects/OpenCvCourse/Resources/Faces/train'):
    p.append(i)
features =[]
labels=[]

def create_train():
    for person in people:
        path=os.path.join(DIR,person)
       # print(path)
        label=people.index(person)
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
        #    print(img_path)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGRA2GRAY)
            face_rect=haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4 )
            for (x,y,w,h) in face_rect:
                face_roi=gray[y:y+h,x:x+w]
                features.append(face_roi)
                labels.append(label)
create_train()

features=np.array(features,dtype="object")
labels=np.array(labels)
face_rec = cv.face.LBPHFaceRecognizer_create()
face_rec.train(features, labels)
face_rec.save("face_trained.yml")
#np.save("features.npy",features)
#np.save("labels.npy",labels)



print(f'lenght of the features= {len(features)}')
print(f'lenght of the labels= {len(labels)}')