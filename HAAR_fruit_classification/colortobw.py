# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    This is a temporary script file.
    
    turn the colorful image into black-white image
    
    
    """


import cv2
import os
import numpy as np

print (cv2.__version__)

path = os.getcwd()
path_before=path+'/pos_ori/'
path_after=path+'/pos_bw/'
f = os.listdir(path_before)


for i in range(len(f)):
    if f[i]!= '.DS_Store':
        img = cv2.imread(path_before+f[i],0)
        print (f[i])
        cv2.imwrite(path_after+f[i],img)


