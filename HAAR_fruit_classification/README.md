step 1    

opencv_createsamples.exe -info ./pos/sample_pos.dat -vec ./pos/sample_pos.vec -num 3 -w 200 -h 200

step 2

opencv_haartraining.exe -data ./cascade -vec ./pos/sample_pos.vec -bg ./neg/sample_neg.dat -nstage 5 -npos 100 -nneg 60 -mem 200 -mode ALL -w 200 -h 200