# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    This is a temporary script file.
    
    recognize the object in the image and cut it into a square image
    
    
    """

import cv2
import os
import numpy as np

print (cv2.__version__)

def crop_image(input_image):
    #高水平梯度和低垂直梯度的图像区域
    cv2.imshow('iii',input_image)
    
    gradX = cv2.Sobel(input_image, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(input_image, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

    # subtract the y-gradient from the x-gradient
    img_gradient = cv2.subtract(gradX, gradY)
    img_gradient = cv2.convertScaleAbs(img_gradient)

    # blur and threshold the image
    blurred = cv2.blur(img_gradient, (9, 9))
    (_, thresh) = cv2.threshold(blurred, 80, 255, cv2.THRESH_BINARY)#_INV)

    #
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # perform a series of erosions and dilations
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

   
    #print (cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE))
    (_,cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]


    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(c)
    #print (cv2.cv.BoxPoints(rect))
    box = np.int0(cv2.boxPoints(rect))


    # draw a bounding box arounded the detected barcode and display the image
    #cv2.drawContours(input_image, [box], -1, (0, 255, 0), 3)


    height,width = input_image.shape


    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    x1_ = (x2-x1)/2-200
    x2_ = (x2-x1)/2+200
    if x1_< 0:
        x1_ = 0
    if x2_ > width:
        x2_ = width
    y1 = min(Ys)
    y2 = max(Ys)
    y1_ = (y2 - y1)/2-200
    y2_ = (y2 - y1)/2+200
    if y1_ < 0:
        y1_ = 0
    if y2_ > height:
        y2_ = height
    #print (int(y1_),y2_,x1_,x2_)
    #cv2.rectangle(input_image,(x1_,y1_),(x2_,y2_),(0,255,0),2) 
    output_image = input_image[int(y1_):int(y2_), int(x1_):int(x2_)]
    return output_image


path = os.getcwd()
path_before=path+'/pos_bw/'
path_after=path+'/pos/'

f = os.listdir(path_before)



print (len(f))


for i in range(len(f)):
#for i in range(1):
    if f[i]== '.DS_Store' or f[i]== 'sample_pos.dat' :
        continue
        #print (f[i])
    input_img = cv2.imread(path_before+f[i],cv2.IMREAD_GRAYSCALE)
    #if input_img.shape[0]>600 and input_img.shape[1]>600:
    output_img = crop_image(input_img)
    cv2.imwrite(path_after+f[i],output_img)
        #print (input_img[200:300,300:400])

        
        
        #for m in range(9,10):
            #for n in range(int(output_img.shape[1]/15)):
                #print(m,',',n,':',output_img[m:m+15,n:n+15])

#j = 0
#while j < 200:
 #   input_img = cv2.imread(f[0],cv2.IMREAD_GRAYSCALE)
  #  output_img = input_img
   # cv2.imwrite('cropImg/%d.bmp'%j,output_img)
    #j += 1










#crop_image(f[0])

