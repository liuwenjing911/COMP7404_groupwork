# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    This is a temporary script file.
    
    
     neg: image to dat file
    
    
    """
#!/usr/bin env python
import os
import cv2

path = os.getcwd()+'/'
pathneg=path+'neg/'

files = os.listdir(pathneg)

n=0
with open(path+'sample_neg.dat','w+') as f:
    for i in range(len(files)):

        if files[i]=='sample_neg.dat' or files[i]=='.DS_Store':
            continue
        
        img = cv2.imread(pathneg+files[i],0)
        f.write('neg/'+files[i]+' 1 75 75 125 125\n')
        n+=1

print (n)



