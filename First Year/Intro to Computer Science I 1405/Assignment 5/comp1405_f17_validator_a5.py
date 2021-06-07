import ast as OO000O0000O0000O0 #line:11
import datetime as O0OO0OOO00000000O #line:12
import pygame as O0O0O0OO00O0000O0 #line:13
from subprocess import call as OOO00OOO0O0O0OO0O #line:14
from os import getcwd as OO0OOO0O0O00OOOOO ,listdir as O000O0O0OO0O00OOO ,path as OO000OOOOOOO0O0O0 ,remove as O0OO00OO0OO0O0O00 ,devnull as OOO00O00OO0OO000O ,rename as O0000OOO0OO00O00O #line:15
from sys import argv as O0OOOO0OO0OO000OO ,exc_info as O00O0O0OO00O00OOO #line:16
from zipfile import ZipFile as O0000OOOO0O0000OO #line:17
from re import match as O0O0O0O00000O00O0 ,sub as OOO0OOOO000O00OOO #line:18
from time import sleep as OOO00OO00OO000OO0 #line:19
CURRENT_CLASS_LIST_FILE ="current_class_list.dat"#line:22
LIST_OF_REQUISITE_FILES =[CURRENT_CLASS_LIST_FILE ]+["kenpixel_mini_square.ttf"]#line:23
LIST_OF_LIBRARY_MODULES =["_liberr.py","_libtui.py","_libprg.py",]#line:28
def clean_current_working_directory ():#line:38
	OOO0OO00O0O0OO00O =O000O0O0OO0O00OOO (OO0OOO0O0O00OOOOO ())#line:40
	for O000O0O0OO0O00O00 in OOO0OO00O0O0OO00O :#line:43
		OO0OOO0O0O00O0O00 =OO000OOOOOOO0O0O0 .join (OO0OOO0O0O00OOOOO (),O000O0O0OO0O00O00 )#line:46
		if not OO000OOOOOOO0O0O0 .isdir (OO0OOO0O0O00O0O00 )and (O000O0O0OO0O00O00 in LIST_OF_REQUISITE_FILES or O000O0O0OO0O00O00 in LIST_OF_LIBRARY_MODULES ):#line:49
			O0OO00OO0OO0O0O00 (O000O0O0OO0O00O00 )#line:51
def exit_program ():#line:61
	clean_current_working_directory ()#line:62
	exit ()#line:63
def validate_submission_header (OO0OO0OOO0O00O0OO ,OO00O000OOOOOO00O ):#line:73
	O0OO0000OOOO0OOOO =open (OO0OO0OOO0O00O0OO ,"r")#line:76
	O000OO000OO00O0OO =[]#line:79
	O0O00O0OOO00OOOOO =False #line:82
	while True :#line:85
		O000O0O0O0OO0O00O =O0OO0000OOOO0OOOO .readline ()#line:88
		if not O000O0O0O0OO0O00O :#line:91
			break #line:92
		if O000O0O0O0OO0O00O .strip ()[:12 ]=="# ==========":#line:95
			if not O0O00O0OOO00OOOOO :#line:96
				O0O00O0OOO00OOOOO =True #line:97
			else :#line:98
				break #line:99
		if O0O00O0OOO00OOOOO :#line:102
			O000OO000OO00O0OO .append (O000O0O0O0OO0O00O .strip ())#line:103
	O0OO0000OOOO0OOOO .close ()#line:106
	OO0O00OOOO0O00OOO =None #line:109
	O00000O0O00OO0O0O =None #line:110
	O00O0OOO000000OOO =""#line:111
	O00OO00000OO00O00 =""#line:112
	for OO0000O0000O0OO0O in O000OO000OO00O0OO :#line:113
		OO0000O0000O0OO0O =OO0000O0000O0OO0O .strip ()#line:116
		if OO0O00OOOO0O00OOO is None :#line:119
			OO0O00OOOO0O00OOO =O0O0O0O00000O00O0 (r"# Student Name \(as it appears on cuLearn\): (.*$)",OO0000O0000O0OO0O )#line:120
			if OO0O00OOOO0O00OOO is not None and len (OO0000O0000O0OO0O )>0 :#line:121
				O00O0OOO000000OOO =OO0O00OOOO0O00OOO .group (1 )#line:122
		if O00000O0O00OO0O0O is None :#line:124
			O00000O0O00OO0O0O =O0O0O0O00000O00O0 (r"# Student ID \(9 digits in angle brackets\): <(\d{9})>",OO0000O0000O0OO0O )#line:125
			if O00000O0O00OO0O0O is not None :#line:126
				O00OO00000OO00O00 =O00000O0O00OO0O0O .group (1 )#line:127
	if O00O0OOO000000OOO is not None and len (O00O0OOO000000OOO )>0 and O00OO00000OO00O00 ==OO00O000OOOOOO00O :#line:129
		return True ,O00O0OOO000000OOO #line:130
	else :#line:131
		return False ,"Student Name Not Found"#line:132
def review_submission_ast (OO0000OOOO0O00O0O ,O00OOOO0O0O0O0000 ):#line:142
	O0O0OO000OO0O0O00 =open (OO0000OOOO0O00O0O ,"r")#line:145
	O00O0OOOOOOO00O00 =O0O0OO000OO0O0O00 .read ()#line:148
	O0O0OO000OO0O0O00 .close ()#line:151
	OO0O0000OOOOOO0O0 =OO000O0000O0000O0 .parse (O00O0OOOOOOO00O00 )#line:154
	O0OOO00O00O00O0OO =[]#line:157
	O0OO0OO0O0OOO0000 =[]#line:158
	for O0OOOO000O000O00O in OO000O0000O0000O0 .walk (OO0O0000OOOOOO0O0 ):#line:161
		if isinstance (O0OOOO000O000O00O ,OO000O0000O0000O0 .Import ):#line:164
			for O00O0000OO0O0O0O0 in O0OOOO000O000O00O .names :#line:165
				O0OOOO000O00000OO =str (O00O0000OO0O0O0O0 .name )#line:166
				if O0OOOO000O00000OO not in O0OO0OO0O0OOO0000 :#line:167
					O0OO0OO0O0OOO0000 .append (O0OOOO000O00000OO )#line:168
		if isinstance (O0OOOO000O000O00O ,OO000O0000O0000O0 .ImportFrom ):#line:171
			O0OOOO000O00000OO =str (O0OOOO000O000O00O .module )#line:172
			if O0OOOO000O00000OO not in O0OO0OO0O0OOO0000 :#line:173
				O0OO0OO0O0OOO0000 .append (O0OOOO000O00000OO )#line:174
			for OOO0O000OO00OO000 in O0OOOO000O000O00O .names :#line:175
				OO000OO00000O000O =str (OOO0O000OO00OO000 .name )#line:176
				if OO000OO00000O000O not in O0OOO00O00O00O0OO :#line:177
					O0OOO00O00O00O0OO .append (OO000OO00000O000O )#line:178
		if isinstance (O0OOOO000O000O00O ,OO000O0000O0000O0 .Call ):#line:181
			if isinstance (O0OOOO000O000O00O .func ,OO000O0000O0000O0 .Name ):#line:182
				OO000OO00000O000O =str (O0OOOO000O000O00O .func .id )#line:183
			elif isinstance (O0OOOO000O000O00O .func ,OO000O0000O0000O0 .Attribute ):#line:184
				OO000OO00000O000O =str (O0OOOO000O000O00O .func .attr )#line:185
			if OO000OO00000O000O not in O0OOO00O00O00O0OO :#line:186
				O0OOO00O00O00O0OO .append (OO000OO00000O000O )#line:187
	return O0OOO00O00O00O0OO ,O0OO0OO0O0OOO0000 #line:189
def main ():#line:200
	clean_current_working_directory ()#line:203
	with O0000OOOO0O0000OO (O0OOOO0OO0OO000OO [0 ].replace ("validator","companion").replace (".py","._z"),"r")as OO0OOO000OO00O0OO :#line:207
		OO0OOO000OO00O0OO .extractall ()#line:208
	import _libprg as _O00O00O00O0OOOOOO #line:211
	O0O0O0O0OO000O00O =open (OOO00O00OO0OO000O ,'w')#line:214
	O0O0OOO00O0OO0O0O =O000O0O0OO0O00OOO (OO0OOO0O0O00OOOOO ())#line:217
	OO000O0O000OOOO0O =False #line:220
	for O00OOOOO0000OO0O0 in O0O0OOO00O0OO0O0O :#line:223
		OO000O00O000O00O0 =O0O0O0O00000O00O0 (r"comp1405_f17_(\d{9})_a5.py",O00OOOOO0000OO0O0 )#line:226
		if OO000O00O000O00O0 is not None :#line:229
			OO000O0O000OOOO0O =True #line:232
			O000O0O0OO0OO00OO =O00OOOOO0000OO0O0 #line:235
			OOOOO0OO0O0OO0O00 =OO000O00O000O00O0 .group (1 )#line:238
			OOOO00OOO0OOOOOO0 ,OOOOOOO0O00000O00 =validate_submission_header (O000O0O0OO0OO00OO ,OOOOO0OO0O0OO0O00 )#line:241
			if OOOO00OOO0OOOOOO0 :#line:243
				try :#line:245
					O0OO000000000000O ="python3 "+O000O0O0OO0OO00OO #line:248
					OOOO0OOO00O0O0000 =OOO00OOO0O0O0OO0O (O0OO000000000000O ,shell =True ,stderr =O0O0O0O0OO000O00O )#line:249
					if not OOOO0OOO00O0O0000 ==0 :#line:252
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
				O000O000000O00OO0 =['*','range','move_down','move_right','move_left','am_i_standing_on','what_number_am_i_standing_on']#line:283
				OO0O0O00O00O0O0O0 =["comp1405_f17_assistant_a5"]#line:286
				OOO0O00O0OOO00000 ,OO00OOO000O00O0OO =review_submission_ast (O000O0O0OO0OO00OO ,OOOOO0OO0O0OO0O00 )#line:289
				OOOOO000O0O00OOO0 =False #line:298
				for O0O0O0O0OOOOO0000 in OOO0O00O0OOO00000 :#line:300
					if O0O0O0O0OOOOO0000 not in O000O000000O00OO0 :#line:301
						OOOOO000O0O00OOO0 =True #line:302
						break #line:303
				if OOOOO000O0O00OOO0 :#line:305
					print ("")#line:306
					print ("     ┌─[ ERROR 96 ]───────────────────────────────────────────────────────┐     ")#line:307
					print ("     │                                                                    │     ")#line:308
					print ("     │ A file with the expected filename was found and executed by the    │     ")#line:309
					print ("     │ validator, but that program used a function that was not           │     ")#line:310
					print ("     │ permitted. Check the generator instructions for the full list of   │     ")#line:311
					print ("     │ functions that you are permitted.                                  │     ")#line:312
					print ("     │                                                                    │     ")#line:313
					print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:314
					print ("")#line:315
					print ("           THE FUNCTIONS LISTED BELOW ARE NOT PERMITTED (OR NECESSARY)          ")#line:316
					print (str ([O000O0OO00O0OO000 for O000O0OO00O0OO000 in OOO0O00O0OOO00000 if O000O0OO00O0OO000 not in O000O000000O00OO0 ]).center (80 ))#line:317
					print ("")#line:318
				OO0OO0OO0O0O0OOOO =False #line:320
				for O0O0O0O0OOOOO0000 in OO00OOO000O00O0OO :#line:322
					if O0O0O0O0OOOOO0000 not in OO0O0O00O00O0O0O0 :#line:323
						OO0OO0OO0O0O0OOOO =True #line:324
						break #line:325
				if OO0OO0OO0O0O0OOOO :#line:327
					print ("")#line:328
					print ("     ┌─[ ERROR 95 ]───────────────────────────────────────────────────────┐     ")#line:329
					print ("     │                                                                    │     ")#line:330
					print ("     │ A file with the expected filename was found and executed by the    │     ")#line:331
					print ("     │ validator, but that program imported a library that was not        │     ")#line:332
					print ("     │ permitted. You should not be importing any additional modules for  │     ")#line:333
					print ("     │ for this assignment.                                               │     ")#line:334
					print ("     │                                                                    │     ")#line:335
					print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:336
					print ("")#line:337
					print ("           THE LIBRARIES LISTED BELOW ARE NOT PERMITTED (OR NECESSARY)          ")#line:338
					print (str ([O000O00OOO000OOO0 for O000O00OOO000OOO0 in OO00OOO000O00O0OO if O000O00OOO000OOO0 not in OO0O0O00O00O0O0O0 ]).center (80 ))#line:339
					print ("")#line:340
			else :#line:343
				print ("")#line:344
				print ("     ┌─[ ERROR 92 ]───────────────────────────────────────────────────────┐     ")#line:345
				print ("     │                                                                    │     ")#line:346
				print ("     │ A file with the expected filename was found and executed by the    │     ")#line:347
				print ("     │ validator, but that program does not appear to include a valid     │     ")#line:348
				print ("     │ header. Reread the instructions provided to you by the generator   │     ")#line:349
				print ("     │ and make sure you follow the header instructions precisely. If     │     ")#line:350
				print ("     │ your header does not exactly match the one that was specified in   │     ")#line:351
				print ("     │ the instructions, the marking program will not be able to find     │     ")#line:352
				print ("     │ your submission and it will receive a mark of 0.                   │     ")#line:353
				print ("     │                                                                    │     ")#line:354
				print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:355
				print ("")#line:356
	if not OO000O0O000OOOO0O :#line:359
		print ("")#line:360
		print ("     ┌─[ ERROR 91 ]───────────────────────────────────────────────────────┐     ")#line:361
		print ("     │                                                                    │     ")#line:362
		print ("     │ A file with the expected filename was not found. Your submission   │     ")#line:363
		print ("     │ must be contained in a file named 'comp1405_f17_#########_a5.py'   │     ")#line:364
		print ("     │ with the number signs replaced by your nine digit student number.  │     ")#line:365
		print ("     │                                                                    │     ")#line:366
		print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:367
		print ("")#line:368
	clean_current_working_directory ()#line:370
	exit_program ()#line:373
if __name__ =="__main__":#line:377
	print ()#line:378
	print ("     THIS PROGRAM WILL NOW REVIEW YOUR SUBMISSION LOOKING FOR COMMON ERRORS     ")#line:379
	print ("     (e.g., INCORRECT FILENAME, MISSING OR INVALID ASSIGNMENT HEADER, etc.)     ")#line:380
	print ()#line:381
	print ("     THIS PROGRAM WILL NOTIFY YOU IF IT DETECTS ANY OF THESE ISSUES, BUT IT     ")#line:382
	print ("     IS NOT 'PRE-MARKING' YOUR SUBMISSION AND IT DOES NOT DETECT ALL ERRORS     ")#line:383
	print ()#line:384
	print ("     IF NO SUCH ISSUES ARE DETECTED THEN NO NOTIFICATIONS WILL BE DISPLAYED     ")#line:385
	print ()#line:386
	print ()#line:387
	print ("     * * PLEASE NOTE THAT THE VALIDATOR FOR THIS ASSIGNMENT IS NOT ABLE * *     ")#line:388
	print ("     * * TO DETERMINE IF YOUR PROGRAM WAS ACTUALLY 'SOLVING' YOUR MAZE. * *     ")#line:389
	print ()#line:390
	main ()