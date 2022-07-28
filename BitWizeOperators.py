import cv2 as cv
import numpy as np
blank=np.zeros((400,400),dtype="uint8")
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow("Circle",circle)
cv.imshow('RECT',rectangle)
#### Bitwize And
bitwize_and=cv.bitwise_and(rectangle,circle)
cv.imshow("bitwizeAnd",bitwize_and)###And operation

### Bitwize OR !intersection regions

bitwize_or=cv.bitwise_or(circle,rectangle)
cv.imshow("OrBitwize",bitwize_or)

### Bitwize XOR
bitwize_xor=cv.bitwise_xor(circle,rectangle)
cv.imshow("BitwizeXor",bitwize_xor)###Non interssction regions

###Bitwize NoT

bitwize_not=cv.bitwise_not(rectangle)# converting 1 to Zero and Zero to 1

cv.imshow("bitwizeNOT",bitwize_not)





cv.waitKey(0)