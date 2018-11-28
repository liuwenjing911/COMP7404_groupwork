# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    This is a temporary script file.
    
    
    pos: image to dat file
    """
#!/usr/bin env python
import os
import cv2
path = os.getcwd()+'/pos/'

files = os.listdir(path)


for i in range(len(files)):
    if files[i]== '.DS_Store' or files[i]=='sample_pos.dat' :
        continue
        #f[i]=path_before+f[i]
    img = cv2.imread(path+files[i],0)
    print (files[i],img.shape)

with open(path+'sample_pos.dat','w+') as f:
    for file in files:
        name = os.path.split(file)
        if name[1]=='sample_pos.dat' or name[1]=='.DS_Store':
            continue
        #print (file)
        #f.write("pos\\"+name[1]+' '+'1 0 0 400 400\n')
        f.write(name[1]+' '+'1 0 0 400 400\n')
        #1 0 0 30 30
        #1 2 2 635 476









#crop_image(f[0])

