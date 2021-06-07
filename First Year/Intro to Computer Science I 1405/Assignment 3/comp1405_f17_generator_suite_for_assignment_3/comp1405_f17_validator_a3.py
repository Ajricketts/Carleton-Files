import ast as O0O00O0OO0000O0OO #line:11
import datetime as O00O0000OO0O0OOOO #line:12
import pygame as O00O0000O00000OO0 #line:13
from subprocess import call as OOOOO0O0OO0OOOOOO #line:14
from os import getcwd as O0OOOOOOOO0O0OOO0 ,listdir as OOOOOO0O0OO0O00OO ,path as O000OOOO0000O0O00 ,remove as O0O0OOO0OOOOO0O0O ,devnull as O0OOO0OO000O0OOOO ,rename as O0O0000OOO0OOOO0O #line:15
from sys import argv as OOOO000O0OOOO0O00 ,exc_info as O0O0O000OO0O000OO #line:16
from zipfile import ZipFile as O00O0OO0000OOOO00 #line:17
from re import match as OOOO0O000O0O00O0O ,sub as OOOO00OOOOOO00O0O #line:18
from time import sleep as O00OO00OOO00O00O0 #line:19
CURRENT_CLASS_LIST_FILE ="current_class_list.dat"#line:22
LIST_OF_REQUISITE_FILES =[CURRENT_CLASS_LIST_FILE ]#line:23
LIST_OF_LIBRARY_MODULES =["_liberr.py","_libtui.py","_libprg.py",]#line:28
'''
This will remove all the files that were extracted from the companion

@params                      none
@return                      none
'''#line:36
def clean_current_working_directory ():#line:37
	O0OO0O0O0OOOO00OO =OOOOOO0O0OO0O00OO (O0OOOOOOOO0O0OOO0 ())#line:39
	for OOOOO0OOO0OOO0OOO in O0OO0O0O0OOOO00OO :#line:42
		O00OOOO0O000O0OOO =O000OOOO0000O0O00 .join (O0OOOOOOOO0O0OOO0 (),OOOOO0OOO0OOO0OOO )#line:45
		if not O000OOOO0000O0O00 .isdir (O00OOOO0O000O0OOO )and (OOOOO0OOO0OOO0OOO in LIST_OF_REQUISITE_FILES or OOOOO0OOO0OOO0OOO in LIST_OF_LIBRARY_MODULES ):#line:48
			O0O0OOO0OOOOO0O0O (OOOOO0OOO0OOO0OOO )#line:50
'''
This is end the program after cleaning the current working directory

@params                      none
@return                      none
'''#line:59
def exit_program ():#line:60
	clean_current_working_directory ()#line:61
	exit ()#line:62
'''
This will verify that the header is present and contains the required information

@params  submission_path     the path to the submission being evaluated
@params  id_in_filename      the id that appears in the filename, for comparison with the header
@return                      a boolean indicating whether the header is acceptable or not
'''#line:71
def validate_submission_header (OOOO00OOOO0OOO000 ,O0OOOO0O0OO0O0OO0 ):#line:72
	O0O00O00OOOOO000O =open (OOOO00OOOO0OOO000 ,"r")#line:75
	OO000OO00OO0OO00O =[]#line:78
	OOO0OO0O0OO00O0O0 =False #line:81
	while True :#line:84
		OO00O00OOO00OOOO0 =O0O00O00OOOOO000O .readline ()#line:87
		if not OO00O00OOO00OOOO0 :#line:90
			break #line:91
		if OO00O00OOO00OOOO0 .strip ()[:12 ]=="# ==========":#line:94
			if not OOO0OO0O0OO00O0O0 :#line:95
				OOO0OO0O0OO00O0O0 =True #line:96
			else :#line:97
				break #line:98
		if OOO0OO0O0OO00O0O0 :#line:101
			OO000OO00OO0OO00O .append (OO00O00OOO00OOOO0 .strip ())#line:102
	O0O00O00OOOOO000O .close ()#line:105
	OOO0O0OO0O0000O00 =None #line:108
	O00OO00O0OO00000O =None #line:109
	O0OOO0O000000000O =""#line:110
	O00O0O0O00O00OOO0 =""#line:111
	for O000OOOO00OOO0OOO in OO000OO00OO0OO00O :#line:112
		O000OOOO00OOO0OOO =O000OOOO00OOO0OOO .strip ()#line:115
		if OOO0O0OO0O0000O00 is None :#line:118
			OOO0O0OO0O0000O00 =OOOO0O000O0O00O0O (r"# Student Name \(as it appears on cuLearn\): (.*$)",O000OOOO00OOO0OOO )#line:119
			if OOO0O0OO0O0000O00 is not None and len (O000OOOO00OOO0OOO )>0 :#line:120
				O0OOO0O000000000O =OOO0O0OO0O0000O00 .group (1 )#line:121
		if O00OO00O0OO00000O is None :#line:123
			O00OO00O0OO00000O =OOOO0O000O0O00O0O (r"# Student ID \(9 digits in angle brackets\): <(\d{9})>",O000OOOO00OOO0OOO )#line:124
			if O00OO00O0OO00000O is not None :#line:125
				O00O0O0O00O00OOO0 =O00OO00O0OO00000O .group (1 )#line:126
	if O0OOO0O000000000O is not None and len (O0OOO0O000000000O )>0 and O00O0O0O00O00OOO0 ==O0OOOO0O0OO0O0OO0 :#line:128
		return True ,O0OOO0O000000000O #line:129
	else :#line:130
		return False ,"Student Name Not Found"#line:131
'''
This will create the abstract syntax tree and process it into lists of features

@params  submission_path     the path to the submission being evaluated
@params  id_in_filename      the id that appears in the filename, for comparison with the header
@return                      the list of functions and modules used in the submission
'''#line:140
def review_submission_ast (O000O00O0OOOOOO00 ,OO00000OO0000000O ):#line:141
	O00OOO000O0OO00OO =open (O000O00O0OOOOOO00 ,"r")#line:144
	O0OOOOOO0OO0OOOO0 =O00OOO000O0OO00OO .read ()#line:147
	O00OOO000O0OO00OO .close ()#line:150
	OO0O00O00000OO000 =O0O00O0OO0000O0OO .parse (O0OOOOOO0OO0OOOO0 )#line:153
	OO0OO0OO00OO000O0 =[]#line:156
	OO0OOOOOO000OOO00 =[]#line:157
	for OO00O00O0O0000OO0 in O0O00O0OO0000O0OO .walk (OO0O00O00000OO000 ):#line:160
		if isinstance (OO00O00O0O0000OO0 ,O0O00O0OO0000O0OO .Import ):#line:163
			for OOO0O0O00O00OO00O in OO00O00O0O0000OO0 .names :#line:164
				O0OO0O0O0O0OO00OO =str (OOO0O0O00O00OO00O .name )#line:165
				if O0OO0O0O0O0OO00OO not in OO0OOOOOO000OOO00 :#line:166
					OO0OOOOOO000OOO00 .append (O0OO0O0O0O0OO00OO )#line:167
		if isinstance (OO00O00O0O0000OO0 ,O0O00O0OO0000O0OO .ImportFrom ):#line:170
			O0OO0O0O0O0OO00OO =str (OO00O00O0O0000OO0 .module )#line:171
			if O0OO0O0O0O0OO00OO not in OO0OOOOOO000OOO00 :#line:172
				OO0OOOOOO000OOO00 .append (O0OO0O0O0O0OO00OO )#line:173
			for OO0OO0O0O0OO000OO in OO00O00O0O0000OO0 .names :#line:174
				O0OO00000OOOOOO0O =str (OO0OO0O0O0OO000OO .name )#line:175
				if O0OO00000OOOOOO0O not in OO0OO0OO00OO000O0 :#line:176
					OO0OO0OO00OO000O0 .append (O0OO00000OOOOOO0O )#line:177
		if isinstance (OO00O00O0O0000OO0 ,O0O00O0OO0000O0OO .Call ):#line:180
			if isinstance (OO00O00O0O0000OO0 .func ,O0O00O0OO0000O0OO .Name ):#line:181
				O0OO00000OOOOOO0O =str (OO00O00O0O0000OO0 .func .id )#line:182
			elif isinstance (OO00O00O0O0000OO0 .func ,O0O00O0OO0000O0OO .Attribute ):#line:183
				O0OO00000OOOOOO0O =str (OO00O00O0O0000OO0 .func .attr )#line:184
			if O0OO00000OOOOOO0O not in OO0OO0OO00OO000O0 :#line:185
				OO0OO0OO00OO000O0 .append (O0OO00000OOOOOO0O )#line:186
	return OO0OO0OO00OO000O0 ,OO0OOOOOO000OOO00 #line:188
'''
This is the main function, primarily responsible for extracting files from the
companion archive and ensuring that the generator will actually able be able
to function with the arguments that have been provided

@params                      none
@return                      none
'''#line:198
def main ():#line:199
	clean_current_working_directory ()#line:202
	with O00O0OO0000OOOO00 (OOOO000O0OOOO0O00 [0 ].replace ("validator","companion").replace (".py","._z"),"r")as O00OOO00OOO0O0OO0 :#line:206
		O00OOO00OOO0O0OO0 .extractall ()#line:207
	import _libprg as _O0OOO00OO00O0OO0O #line:210
	OO00O0OO0O000OO00 =open (O0OOO0OO000O0OOOO ,'w')#line:213
	OOOOO000OOO000OOO =OOOOOO0O0OO0O00OO (O0OOOOOOOO0O0OOO0 ())#line:216
	O0OO0O0O00OO00OOO =False #line:219
	for O0OO0OOOOOO000O0O in OOOOO000OOO000OOO :#line:222
		O0O00000O0OOO00O0 =OOOO0O000O0O00O0O (r"comp1405_f17_(\d{9})_a3.py",O0OO0OOOOOO000O0O )#line:225
		if O0O00000O0OOO00O0 is not None :#line:228
			O0OO0O0O00OO00OOO =True #line:231
			O0O0O00OO0O0OOO0O =O0OO0OOOOOO000O0O #line:234
			OOOOOOOO0O0O0000O =O0O00000O0OOO00O0 .group (1 )#line:237
			OOO00O0O00O000OO0 ,OO00O0OOO00OO0OO0 =validate_submission_header (O0O0O00OO0O0OOO0O ,OOOOOOOO0O0O0000O )#line:240
			if OOO00O0O00O000OO0 :#line:242
				try :#line:245
					O00OOOO0000000O0O ="python3 "+O0O0O00OO0O0OOO0O #line:248
					O0OOO000O00OOOO00 =OOOOO0O0OO0OOOOOO (O00OOOO0000000O0O ,shell =True ,stderr =OO00O0OO0O000OO00 )#line:249
					if not O0OOO000O00OOOO00 ==0 :#line:252
						print ("")#line:254
						print ("     ┌─[ ERROR 99 ]───────────────────────────────────────────────────────┐     ")#line:255
						print ("     │                                                                    │     ")#line:256
						print ("     │ A file with the expected filename was found but when the validator │     ")#line:257
						print ("     │ attempted to run that program, it crashed. Ensure that the source  │     ")#line:258
						print ("     │ file you have been working on was named correctly and does not     │     ")#line:259
						print ("     │ crash on execution.                                                │     ")#line:260
						print ("     │                                                                    │     ")#line:261
						print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:262
						print ("")#line:263
				except :#line:265
					print ("")#line:266
					print ("     ┌─[ ERROR 99 ]───────────────────────────────────────────────────────┐     ")#line:267
					print ("     │                                                                    │     ")#line:268
					print ("     │ A file with the expected filename was found but when the validator │     ")#line:269
					print ("     │ attempted to run that program, it crashed. Ensure that the source  │     ")#line:270
					print ("     │ file you have been working on was named correctly and does not     │     ")#line:271
					print ("     │ crash on execution.                                                │     ")#line:272
					print ("     │                                                                    │     ")#line:273
					print ("     │ Please also note that the validator was only designed to function  │     ")#line:274
					print ("     │ on the virtual machine. Attempting to run the validator from any   │     ")#line:275
					print ("     │ other operating system may result in this error.                   │     ")#line:276
					print ("     │                                                                    │     ")#line:277
					print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:278
					print ("")#line:279
				_O0OOO00OO00O0OO0O .set_random_source (OOOOOOOO0O0O0000O )#line:282
				O0OOO00000OOO00OO =["circle","square","diamond","cross","triangle","pentagon"]#line:284
				O0O000O0OO0OOOO0O =["red","orange","green","blue","purple","black"]#line:285
				O0OOOOO00OO0O0000 =["is_inside_a_","wrapped_in_a_","is_shaped_like_a_"]#line:286
				OO0OO0OOO0000OO0O =["is_colored_","color_is_","painted_"]#line:287
				OO0O0OOOOOOO000O0 =["is_divisible_by","evenly_divides_by","divides_evenly_by"]#line:288
				OO0OOOO00O00OO00O =O0OOOOO00OO0O0000 [_O0OOO00OO00O0OO0O .get_random_integer (0 ,2 )]#line:290
				OO0000O000000O0OO =OO0OO0OOO0000OO0O [_O0OOO00OO00O0OO0O .get_random_integer (0 ,2 )]#line:291
				O0OO0OOO00OO0OOOO =OO0O0OOOOOOO000O0 [_O0OOO00OO00O0OO0O .get_random_integer (0 ,2 )]#line:292
				O00OOOO0OOO000OOO =[OO0OOOO00O00OO00O +OO0OO0000O0O0000O +"(e)"for OO0OO0000O0O0000O in O0OOO00000OOO00OO ]+[OO0000O000000O0OO +O0O0OOO0O00000OOO +"(e)"for O0O0OOO0O00000OOO in O0O000O0OO0OOOO0O ]+[O0OO0OOO00OO0OOOO +"(e, d)"]#line:294
				O0O0OOO000O0OO000 =[OO0OOOO00O00OO00O +OO00O00O0OOOO0OO0 for OO00O00O0OOOO0OO0 in O0OOO00000OOO00OO ]+[OO0000O000000O0OO +O000O00OO0000OO00 for O000O00OO0000OO00 in O0O000O0OO0OOOO0O ]+[O0OO0OOO00OO0OOOO ]#line:296
				O0O000OOO0OOO0O0O =['*','run_the_program']+O0O0OOO000O0OO000 #line:299
				O0O0O0O0O00OO00OO =["comp1405_f17_assistant_a3"]#line:302
				OO000OO0OO0OO0OOO ,OOOOOOOOOOOO0000O =review_submission_ast (O0O0O00OO0O0OOO0O ,OOOOOOOO0O0O0000O )#line:305
				for OOOO00O0OO0OOO00O in OO000OO0OO0OO0OOO :#line:314
					if OOOO00O0OO0OOO00O not in O0O000OOO0OOO0O0O :#line:315
						print ("")#line:316
						print ("     ┌─[ ERROR 96 ]───────────────────────────────────────────────────────┐     ")#line:317
						print ("     │                                                                    │     ")#line:318
						print ("     │ A file with the expected filename was found and executed by the    │     ")#line:319
						print ("     │ validator, but that program used a function that was not           │     ")#line:320
						print ("     │ permitted. Check the generator instructions for the full list of   │     ")#line:321
						print ("     │ functions that you are permitted.                                  │     ")#line:322
						print ("     │                                                                    │     ")#line:323
						print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:324
						print ("")#line:325
						print ("           THE FUNCTIONS LISTED BELOW ARE NOT PERMITTED (OR NECESSARY)          ")#line:326
						print (str ([O0OOO00OOOO00O0OO for O0OOO00OOOO00O0OO in OO000OO0OO0OO0OOO if O0OOO00OOOO00O0OO not in O0O000OOO0OOO0O0O ]).center (80 ))#line:327
						print ("")#line:328
				for OOOO00O0OO0OOO00O in OOOOOOOOOOOO0000O :#line:331
					if OOOO00O0OO0OOO00O not in O0O0O0O0O00OO00OO :#line:332
						print ("")#line:333
						print ("     ┌─[ ERROR 95 ]───────────────────────────────────────────────────────┐     ")#line:334
						print ("     │                                                                    │     ")#line:335
						print ("     │ A file with the expected filename was found and executed by the    │     ")#line:336
						print ("     │ validator, but that program imported a library that was not        │     ")#line:337
						print ("     │ permitted. You should not be importing any additional modules for  │     ")#line:338
						print ("     │ for this assignment.                                               │     ")#line:339
						print ("     │                                                                    │     ")#line:340
						print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:341
						print ("")#line:342
						print ("           THE LIBRARIES LISTED BELOW ARE NOT PERMITTED (OR NECESSARY)          ")#line:343
						print (str ([O0000OOO0OO00O00O for O0000OOO0OO00O00O in OOOOOOOOOOOO0000O if O0000OOO0OO00O00O not in O0O0O0O0O00OO00OO ]).center (80 ))#line:344
						print ("")#line:345
			else :#line:348
				print ("")#line:349
				print ("     ┌─[ ERROR 92 ]───────────────────────────────────────────────────────┐     ")#line:350
				print ("     │                                                                    │     ")#line:351
				print ("     │ A file with the expected filename was found and executed by the    │     ")#line:352
				print ("     │ validator, but that program does not appear to include a valid     │     ")#line:353
				print ("     │ header. Reread the instructions provided to you by the generator   │     ")#line:354
				print ("     │ and make sure you follow the header instructions precisely. If     │     ")#line:355
				print ("     │ your header does not exactly match the one that was specified in   │     ")#line:356
				print ("     │ the instructions, the marking program will not be able to find     │     ")#line:357
				print ("     │ your submission and it will receive a mark of 0.                   │     ")#line:358
				print ("     │                                                                    │     ")#line:359
				print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:360
				print ("")#line:361
	if not O0OO0O0O00OO00OOO :#line:364
		print ("")#line:365
		print ("     ┌─[ ERROR 91 ]───────────────────────────────────────────────────────┐     ")#line:366
		print ("     │                                                                    │     ")#line:367
		print ("     │ A file with the expected filename was not found. Your submission   │     ")#line:368
		print ("     │ must be contained in a file named 'comp1405_f17_#########_a3.py'   │     ")#line:369
		print ("     │ with the number signs replaced by your nine digit student number.  │     ")#line:370
		print ("     │                                                                    │     ")#line:371
		print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:372
		print ("")#line:373
	exit_program ()#line:376
''' the (only) "top-level" code in the generator for calling main() '''#line:379
if __name__ =="__main__":#line:380
	print ()#line:381
	print ("     THIS PROGRAM WILL NOW REVIEW YOUR SUBMISSION LOOKING FOR COMMON ERRORS     ")#line:382
	print ("     (e.g., INCORRECT FILENAME, MISSING OR INVALID ASSIGNMENT HEADER, etc.)     ")#line:383
	print ()#line:384
	print ("     THIS PROGRAM WILL NOTIFY YOU IF IT DETECTS ANY OF THESE ISSUES, BUT IT     ")#line:385
	print ("     IS NOT 'PRE-MARKING' YOUR SUBMISSION AND IT DOES NOT DETECT ALL ERRORS     ")#line:386
	print ()#line:387
	print ("     IF NO SUCH ISSUES ARE DETECTED THEN NO NOTIFICATIONS WILL BE DISPLAYED     ")#line:388
	print ()#line:389
	main ()