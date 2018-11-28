# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    This is a temporary script file.
    """

import cv2
import os
import numpy as np

print (cv2.__version__)


path = os.getcwd()
path_before=path+'/testwp/'
path_r=path+'/cut/'
path2=path+'/pineapple/haar_pineapple.xml'
f = os.listdir(path_before)


cascade = cv2.CascadeClassifier('haar_pineapple.xml')
cascade.load(path2)

print (path2)


print (f[1])
img = cv2.imread(path_before+f[1])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#cv2.namedWindow("img");
#cv2.imshow("image", img);
#cv2.imshow('img',gray)

#face=face_cascade.detectMultiScale(gray)
faces = cascade.detectMultiScale(gray,# detector options
                                 scaleFactor = 1.1,
                                 minNeighbors = 5,
                                 minSize = (50, 50))


i=0

for (x, y, w, h) in faces:
    i+=1
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    temp=img[y:y+h,x:x+w,:]
    cv2.imwrite('%s_%d.jpg'%(os.path.basename(path_r).split('.')[0],i),temp)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
