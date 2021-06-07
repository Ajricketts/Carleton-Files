import ast as O0O000O0O0O00OOO0 #line:11
import datetime as OOOO00OO0OO00O0OO #line:12
import pygame as OO00OO0000O0OOO00 #line:13
from subprocess import call as O0OOO0000O000000O #line:14
from os import getcwd as OOO0O00000O0O00O0 ,listdir as O000O0O0O0OOOOOOO ,path as O00OO0O0OO0OO0O00 ,remove as OO0O000O0OOOOOOOO ,devnull as OO0O0O00OOO0O00OO ,rename as OOOO0OO0OOOOOOO0O #line:15
from sys import argv as O000O00000O00O00O ,exc_info as OO00O0O000000O0O0 #line:16
from zipfile import ZipFile as OO0O00O0O00O00000 #line:17
from re import match as O00OO00O0OO0O000O ,sub as O0O0OO000O0OO000O #line:18
from time import sleep as OOO0O00O0O0O00OOO #line:19
CURRENT_CLASS_LIST_FILE ="current_class_list.dat"#line:22
LIST_OF_REQUISITE_FILES =[CURRENT_CLASS_LIST_FILE ]+["guesswho_earring.png","guesswho_eyepatch.png","guesswho_face.png","guesswho_glasses.png","guesswho_hair.png","guesswho_hat.png","guesswho_moustache.png","guesswho_pipe.png","guesswho_tattoo.png","guesswho_tie.png"]#line:23
LIST_OF_LIBRARY_MODULES =["_liberr.py","_libtui.py","_libprg.py",]#line:28
'''
This will remove all the files that were extracted from the companion

@params                      none
@return                      none
'''#line:37
def clean_current_working_directory ():#line:38
	OO00OOO0000OO0OOO =O000O0O0O0OOOOOOO (OOO0O00000O0O00O0 ())#line:40
	for O00OO00O00000O0O0 in OO00OOO0000OO0OOO :#line:43
		OOO0O00O0O000OOOO =O00OO0O0OO0OO0O00 .join (OOO0O00000O0O00O0 (),O00OO00O00000O0O0 )#line:46
		if not O00OO0O0OO0OO0O00 .isdir (OOO0O00O0O000OOOO )and (O00OO00O00000O0O0 in LIST_OF_REQUISITE_FILES or O00OO00O00000O0O0 in LIST_OF_LIBRARY_MODULES ):#line:49
			OO0O000O0OOOOOOOO (O00OO00O00000O0O0 )#line:51
'''
This is end the program after cleaning the current working directory

@params                      none
@return                      none
'''#line:60
def exit_program ():#line:61
	clean_current_working_directory ()#line:62
	exit ()#line:63
'''
This will verify that the header is present and contains the required information

@params  submission_path     the path to the submission being evaluated
@params  id_in_filename      the id that appears in the filename, for comparison with the header
@return                      a boolean indicating whether the header is acceptable or not
'''#line:72
def validate_submission_header (O0000OO0OO00O00OO ,OOO0OOO0O0O000O0O ):#line:73
	OO00OO0O00OO0OO0O =open (O0000OO0OO00O00OO ,"r")#line:76
	O00O00000O00OO00O =[]#line:79
	OO0O0O00O00000OO0 =False #line:82
	while True :#line:85
		OO0O0O000OOOOOOOO =OO00OO0O00OO0OO0O .readline ()#line:88
		if not OO0O0O000OOOOOOOO :#line:91
			break #line:92
		if OO0O0O000OOOOOOOO .strip ()[:12 ]=="# ==========":#line:95
			if not OO0O0O00O00000OO0 :#line:96
				OO0O0O00O00000OO0 =True #line:97
			else :#line:98
				break #line:99
		if OO0O0O00O00000OO0 :#line:102
			O00O00000O00OO00O .append (OO0O0O000OOOOOOOO .strip ())#line:103
	OO00OO0O00OO0OO0O .close ()#line:106
	O000OO000O0OOO000 =None #line:109
	O00OO000O00O00O0O =None #line:110
	OO0000000O0O0O0OO =""#line:111
	OO0O0O000000OO0O0 =""#line:112
	for O00OOOOO000O00O0O in O00O00000O00OO00O :#line:113
		O00OOOOO000O00O0O =O00OOOOO000O00O0O .strip ()#line:116
		if O000OO000O0OOO000 is None :#line:119
			O000OO000O0OOO000 =O00OO00O0OO0O000O (r"# Student Name \(as it appears on cuLearn\): (.*$)",O00OOOOO000O00O0O )#line:120
			if O000OO000O0OOO000 is not None and len (O00OOOOO000O00O0O )>0 :#line:121
				OO0000000O0O0O0OO =O000OO000O0OOO000 .group (1 )#line:122
		if O00OO000O00O00O0O is None :#line:124
			O00OO000O00O00O0O =O00OO00O0OO0O000O (r"# Student ID \(9 digits in angle brackets\): <(\d{9})>",O00OOOOO000O00O0O )#line:125
			if O00OO000O00O00O0O is not None :#line:126
				OO0O0O000000OO0O0 =O00OO000O00O00O0O .group (1 )#line:127
	if OO0000000O0O0O0OO is not None and len (OO0000000O0O0O0OO )>0 and OO0O0O000000OO0O0 ==OOO0OOO0O0O000O0O :#line:129
		return True ,OO0000000O0O0O0OO #line:130
	else :#line:131
		return False ,"Student Name Not Found"#line:132
'''
This will create the abstract syntax tree and process it into lists of features

@params  submission_path     the path to the submission being evaluated
@params  id_in_filename      the id that appears in the filename, for comparison with the header
@return                      the list of functions and modules used in the submission
'''#line:141
def review_submission_ast (OO0OO00O0OO0000O0 ,O0000O0OO00OOOOOO ):#line:142
	OO0O00000O00OOO0O =open (OO0OO00O0OO0000O0 ,"r")#line:145
	O0O00O0O0000O0000 =OO0O00000O00OOO0O .read ()#line:148
	OO0O00000O00OOO0O .close ()#line:151
	OO0000OO0O0O00O0O =O0O000O0O0O00OOO0 .parse (O0O00O0O0000O0000 )#line:154
	OO00000OO0000OOO0 =[]#line:157
	O000000O00OO000OO =[]#line:158
	for OOOOO00OO00OO0OO0 in O0O000O0O0O00OOO0 .walk (OO0000OO0O0O00O0O ):#line:161
		if isinstance (OOOOO00OO00OO0OO0 ,O0O000O0O0O00OOO0 .Import ):#line:164
			for O0000000OOOOO00O0 in OOOOO00OO00OO0OO0 .names :#line:165
				OO0000OO000O00OOO =str (O0000000OOOOO00O0 .name )#line:166
				if OO0000OO000O00OOO not in O000000O00OO000OO :#line:167
					O000000O00OO000OO .append (OO0000OO000O00OOO )#line:168
		if isinstance (OOOOO00OO00OO0OO0 ,O0O000O0O0O00OOO0 .ImportFrom ):#line:171
			OO0000OO000O00OOO =str (OOOOO00OO00OO0OO0 .module )#line:172
			if OO0000OO000O00OOO not in O000000O00OO000OO :#line:173
				O000000O00OO000OO .append (OO0000OO000O00OOO )#line:174
			for OO000OOOO00O00OO0 in OOOOO00OO00OO0OO0 .names :#line:175
				O0OO00OOOO000O000 =str (OO000OOOO00O00OO0 .name )#line:176
				if O0OO00OOOO000O000 not in OO00000OO0000OOO0 :#line:177
					OO00000OO0000OOO0 .append (O0OO00OOOO000O000 )#line:178
		if isinstance (OOOOO00OO00OO0OO0 ,O0O000O0O0O00OOO0 .Call ):#line:181
			if isinstance (OOOOO00OO00OO0OO0 .func ,O0O000O0O0O00OOO0 .Name ):#line:182
				O0OO00OOOO000O000 =str (OOOOO00OO00OO0OO0 .func .id )#line:183
			elif isinstance (OOOOO00OO00OO0OO0 .func ,O0O000O0O0O00OOO0 .Attribute ):#line:184
				O0OO00OOOO000O000 =str (OOOOO00OO00OO0OO0 .func .attr )#line:185
			if O0OO00OOOO000O000 not in OO00000OO0000OOO0 :#line:186
				OO00000OO0000OOO0 .append (O0OO00OOOO000O000 )#line:187
	return OO00000OO0000OOO0 ,O000000O00OO000OO #line:189
'''
This is the main function, primarily responsible for extracting files from the
companion archive and ensuring that the generator will actually able be able
to function with the arguments that have been provided

@params                      none
@return                      none
'''#line:199
def main ():#line:200
	clean_current_working_directory ()#line:203
	with OO0O00O0O00O00000 (O000O00000O00O00O [0 ].replace ("validator","companion").replace (".py","._z"),"r")as OOOO0000OO00O0OOO :#line:207
		OOOO0000OO00O0OOO .extractall ()#line:208
	import _libprg as _OOOO00O0O0OO000O0 #line:211
	O00OOOO0O0O0O0O0O =open (OO0O0O00OOO0O00OO ,'w')#line:214
	O000000OO00O0O00O =O000O0O0O0OOOOOOO (OOO0O00000O0O00O0 ())#line:217
	O0O0OOOO000OOOO0O =False #line:220
	for O0000O000000OO00O in O000000OO00O0O00O :#line:223
		O0OOO000O0O00OOOO =O00OO00O0OO0O000O (r"comp1405_f17_(\d{9})_a4.py",O0000O000000OO00O )#line:226
		if O0OOO000O0O00OOOO is not None :#line:229
			O0O0OOOO000OOOO0O =True #line:232
			OOO0O00O0000OOOOO =O0000O000000OO00O #line:235
			O0000000O0O0000O0 =O0OOO000O0O00OOOO .group (1 )#line:238
			OOO0OOOOO000OO0OO ,O0O0O00OOOOO00O0O =validate_submission_header (OOO0O00O0000OOOOO ,O0000000O0O0000O0 )#line:241
			if OOO0OOOOO000OO0OO :#line:243
				OO00O0OOO0O00O000 =['*','upper','lower','ask_question','make_a_guess']#line:284
				O00O0OO000OOO0OO0 =["comp1405_f17_assistant_a4"]#line:287
				O00OO0000O0O000OO ,OOOO000OOO0OOO0OO =review_submission_ast (OOO0O00O0000OOOOO ,O0000000O0O0000O0 )#line:290
				for O00OOOOO00OOOO00O in O00OO0000O0O000OO :#line:299
					if O00OOOOO00OOOO00O not in OO00O0OOO0O00O000 :#line:300
						print ("")#line:301
						print ("     ┌─[ ERROR 96 ]───────────────────────────────────────────────────────┐     ")#line:302
						print ("     │                                                                    │     ")#line:303
						print ("     │ A file with the expected filename was found and executed by the    │     ")#line:304
						print ("     │ validator, but that program used a function that was not           │     ")#line:305
						print ("     │ permitted. Check the generator instructions for the full list of   │     ")#line:306
						print ("     │ functions that you are permitted.                                  │     ")#line:307
						print ("     │                                                                    │     ")#line:308
						print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:309
						print ("")#line:310
						print ("           THE FUNCTIONS LISTED BELOW ARE NOT PERMITTED (OR NECESSARY)          ")#line:311
						print (str ([OOO0OOO000OO00000 for OOO0OOO000OO00000 in O00OO0000O0O000OO if OOO0OOO000OO00000 not in OO00O0OOO0O00O000 ]).center (80 ))#line:312
						print ("")#line:313
				for O00OOOOO00OOOO00O in OOOO000OOO0OOO0OO :#line:316
					if O00OOOOO00OOOO00O not in O00O0OO000OOO0OO0 :#line:317
						print ("")#line:318
						print ("     ┌─[ ERROR 95 ]───────────────────────────────────────────────────────┐     ")#line:319
						print ("     │                                                                    │     ")#line:320
						print ("     │ A file with the expected filename was found and executed by the    │     ")#line:321
						print ("     │ validator, but that program imported a library that was not        │     ")#line:322
						print ("     │ permitted. You should not be importing any additional modules for  │     ")#line:323
						print ("     │ for this assignment.                                               │     ")#line:324
						print ("     │                                                                    │     ")#line:325
						print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:326
						print ("")#line:327
						print ("           THE LIBRARIES LISTED BELOW ARE NOT PERMITTED (OR NECESSARY)          ")#line:328
						print (str ([OOO0OOOO000OOO0OO for OOO0OOOO000OOO0OO in OOOO000OOO0OOO0OO if OOO0OOOO000OOO0OO not in O00O0OO000OOO0OO0 ]).center (80 ))#line:329
						print ("")#line:330
			else :#line:333
				print ("")#line:334
				print ("     ┌─[ ERROR 92 ]───────────────────────────────────────────────────────┐     ")#line:335
				print ("     │                                                                    │     ")#line:336
				print ("     │ A file with the expected filename was found and executed by the    │     ")#line:337
				print ("     │ validator, but that program does not appear to include a valid     │     ")#line:338
				print ("     │ header. Reread the instructions provided to you by the generator   │     ")#line:339
				print ("     │ and make sure you follow the header instructions precisely. If     │     ")#line:340
				print ("     │ your header does not exactly match the one that was specified in   │     ")#line:341
				print ("     │ the instructions, the marking program will not be able to find     │     ")#line:342
				print ("     │ your submission and it will receive a mark of 0.                   │     ")#line:343
				print ("     │                                                                    │     ")#line:344
				print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:345
				print ("")#line:346
	if not O0O0OOOO000OOOO0O :#line:349
		print ("")#line:350
		print ("     ┌─[ ERROR 91 ]───────────────────────────────────────────────────────┐     ")#line:351
		print ("     │                                                                    │     ")#line:352
		print ("     │ A file with the expected filename was not found. Your submission   │     ")#line:353
		print ("     │ must be contained in a file named 'comp1405_f17_#########_a4.py'   │     ")#line:354
		print ("     │ with the number signs replaced by your nine digit student number.  │     ")#line:355
		print ("     │                                                                    │     ")#line:356
		print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:357
		print ("")#line:358
	clean_current_working_directory ()#line:360
	exit_program ()#line:363
''' the (only) "top-level" code in the generator for calling main() '''#line:366
if __name__ =="__main__":#line:367
	print ()#line:368
	print ("     THIS PROGRAM WILL NOW REVIEW YOUR SUBMISSION LOOKING FOR COMMON ERRORS     ")#line:369
	print ("     (e.g., INCORRECT FILENAME, MISSING OR INVALID ASSIGNMENT HEADER, etc.)     ")#line:370
	print ()#line:371
	print ("     THIS PROGRAM WILL NOTIFY YOU IF IT DETECTS ANY OF THESE ISSUES, BUT IT     ")#line:372
	print ("     IS NOT 'PRE-MARKING' YOUR SUBMISSION AND IT DOES NOT DETECT ALL ERRORS     ")#line:373
	print ()#line:374
	print ("     IF NO SUCH ISSUES ARE DETECTED THEN NO NOTIFICATIONS WILL BE DISPLAYED     ")#line:375
	print ()#line:376
	print ()#line:377
	print ("     * * PLEASE NOTE THAT THE VALIDATOR FOR THIS ASSIGNMENT IS NOT ABLE * *     ")#line:378
	print ("     * * TO RUN YOUR SUBMISSION (SINCE IT CAN'T ACTUALLY PLAY THE GAME) * *     ")#line:379
	print ("     * * SO YOU MUST CONFIRM FOR YOURSELF THAT YOUR SUBMISSION DOES NOT * *     ")#line:380
	print ("     * * CRASH UPON EXECUTION. A SUBMISSION THAT CRASHES RECEIVES ZERO. * *     ")#line:381
	print ()#line:382
	main ()
#e9015584e6a44b14988f13e2298bcbf9


#===============================================================#
# Obfuscated by Oxyry Python Obfuscator (http://pyob.oxyry.com) #
#===============================================================#
