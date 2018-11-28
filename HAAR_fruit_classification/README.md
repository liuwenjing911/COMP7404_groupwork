Part1 Preprocessing:   
In this part, process raw images   
Step1:
Use colortobw.py to convert the colourful image into black-white image.   

Step2:
Use cut.py to get the object position in the image and cut the image into suitable size.   

Step3:
Use postodat.py to generating the dat file for positive images.  

Step4:
Use negtodat.py to generating the dat file for negative images.        

If the number of negative images is smaller than requirement, negcut can be used to cut the negative images and increase the number of negative images.    



Part 2 Generating XML:
In this part, DOS will be used. In the DOS window, the commands below will be run successively.

step 1
generating vec file for positive images and compress the images, run the command.
command:
opencv_createsamples.exe -info ./pos/sample_pos.dat -vec ./pos/sample_pos.vec -num 300 -w 20 -h 20

step 2
Haar-Trainning to generating classifier, run the command.
command:
opencv_haartraining.exe -data data -vec pos/sample_pos.vec -bg sample_neg.dat -nstage 20 -npos 300 -nneg 1000 -mem 200 -mode ALL -w 20 -h 20

step 3
Create the XML file, run the command.
command:
haarconv.exe data haar_pineapple.xml 25 25    



Part 3 Detection

Use test.py to detect the objects in one image.    
