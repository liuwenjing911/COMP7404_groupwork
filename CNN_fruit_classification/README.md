#Fruit_classification

the fruit_classification project contains two files: train.py and test.py

 train.py have two inputs				 and two outputs
 	train_dir : train pictures				json_file : outputs direction of *.json
	test_dir  : test pictures				weights	  : outputs direction of *.h5


 test.py have three inputs				and one output
	img_filename : inout picrure
	json_file	 : *.json file
	weights		 : *.h5 file




 train.py construct 5-layer netural networks based on the RGB of the picture
 after calculation, it can calculate *.json and *.h5 file
 *.json : The model convert to JSON format
 *.h5   ：The network weights are written to h5 format


