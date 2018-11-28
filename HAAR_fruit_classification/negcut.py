# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    This is a temporary script file.
    """
#!/usr/bin env python
import os
from PIL import Image
import cv2

def splitimage(src, rownum, colnum, dstpath):
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('开始处理图片切割, 请稍候...')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                

                img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext), ext)
                num = num + 1





        print('图片切割完毕，共生成 %s 张小图片。' % num)
    else:
        print('不合法的行列切割参数！')
        
        
path = os.getcwd()
path_before=path+'/neg_a1/'
path_after=path+'/neg_a1/'

f = os.listdir(path_before)

for i in range(len(f)):
#for i in range(1):
    if f[i]== '.DS_Store' or f[i]== 'neg.dat' :
        continue
    print (f[i])
    src = path_before+f[i]
    dstpath = path_after
    
    input_img = cv2.imread(path_before+f[i],0)
    
    print ('--',input_img)
    (h,w)=input_img.shape
    #h,w=input_img.shape
    
    row = int(h/200)
    col = int(w/200)
    if row > 0 and col > 0:
        splitimage(src, row, col, dstpath)
    else:
            print('无效的行列切割参数！')

else:
    print('图片文件 %s 不存在！' % src)






#crop_image(f[0])

