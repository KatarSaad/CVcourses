### REading images and videos was first on the list
### then we learned to rescale input wth rescale(frame,scale=default) method
###rescale works on evry type of input ### resize works only on images


###Then we learned to draw shapes and text :like rectangle and text


####The essential functions are :
     ###turning images to the gray scale
     ###bluring images is usefull too (effet flow )
     ####canny is edge cascade tool/it s great
     ###dialating the images is dialating the edges and making them thicker
     ###eroded will take the dialated image i dont know the meaning yet
     ###croping imagse too is usefull
     ###rotation and translating the images

###Contour detecting
     ####cv.findCountour()-->takes canny or blured canny to find list of cordinantes of contours
     ####threashold atemps to binarrys an image (1,0)(Black,white ) with a specific threshold
     ####we can draw in blank image with method cv.drawContours()

