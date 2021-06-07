from os import getcwd as OOO000OOOO0OO0O0O ,listdir as O00O00O00O000O0O0 ,path as O0OO000OOO0O0OO00 ,remove as O000O0000000O0O0O #line:2
from sys import argv as OOO000OOOO0O0OO0O #line:3
from zipfile import ZipFile as OOO0O0O00OO0O0000 #line:4
import textwrap as OO000O0OOOO00000O #line:5
CURRENT_CLASS_LIST_FILE ="current_class_list.dat"#line:8
LIST_OF_REQUISITE_FILES =[CURRENT_CLASS_LIST_FILE ]#line:9
LIST_OF_LIBRARY_MODULES =["_liberr.py","_libtui.py","_libprg.py",]#line:14
'''
This will remove all the files that were extracted from the companion

@params                      none
@return                      none
'''#line:22
def clean_current_working_directory ():#line:23
	OOOOO0O00O000OO00 =O00O00O00O000O0O0 (OOO000OOOO0OO0O0O ())#line:25
	for OO00OOOO0O0O00000 in OOOOO0O00O000OO00 :#line:28
		OOO0OOOO000O0O0O0 =O0OO000OOO0O0OO00 .join (OOO000OOOO0OO0O0O (),OO00OOOO0O0O00000 )#line:31
		if not O0OO000OOO0O0OO00 .isdir (OOO0OOOO000O0O0O0 )and (OO00OOOO0O0O00000 in LIST_OF_REQUISITE_FILES or OO00OOOO0O0O00000 in LIST_OF_LIBRARY_MODULES ):#line:34
			O000O0000000O0O0O (OO00OOOO0O0O00000 )#line:36
'''
This is end the program after cleaning the current working directory

@params                      none
@return                      none
'''#line:44
def exit_program ():#line:45
	clean_current_working_directory ()#line:46
	exit ()#line:47
'''
This is the actual instruction generator that is specific to this assignment

@params                      none
@return                      none
'''#line:55
def generate_assignment_instructions (OO000O0000O00OOOO ):#line:56
	import _libprg as _OO0O00OO0000OOO0O #line:58
	_OO0O00OO0000OOO0O .set_random_source (OO000O0000O00OOOO )#line:60
	O00O00OO0OOO0OO0O =["circle","square","diamond","cross","triangle","pentagon"]#line:62
	O0OOOO0O0O0O00OO0 =["red","orange","green","blue","purple","black"]#line:63
	O0OO0O0OOO0000OOO =["is_inside_a_","wrapped_in_a_","is_shaped_like_a_"]#line:64
	O00OO0OOO0OOO0O00 =["is_colored_","color_is_","painted_"]#line:65
	O000O00O000000OOO =["is_divisible_by","evenly_divides_by","divides_evenly_by"]#line:66
	OO0O0O0OO0O000OOO =O0OO0O0OOO0000OOO [_OO0O00OO0000OOO0O .get_random_integer (0 ,2 )]#line:68
	OOOO0O0O0O0OOO000 =O00OO0OOO0OOO0O00 [_OO0O00OO0000OOO0O .get_random_integer (0 ,2 )]#line:69
	OO0O0O00OOO000OO0 =O000O00O000000OOO [_OO0O00OO0000OOO0O .get_random_integer (0 ,2 )]#line:70
	OOOOO0OO00O000OOO =[OO0O0O0OO0O000OOO +O0000000O000OO0OO +"(e)"for O0000000O000OO0OO in O00O00OO0OOO0OO0O ]+[OOOO0O0O0O0OOO000 +O0OO0OO0000OO0OO0 +"(e)"for O0OO0OO0000OO0OO0 in O0OOOO0O0O0O00OO0 ]+[OO0O0O00OOO000OO0 +"(e, d)"]#line:72
	OO0O000O0OOO00OOO =OOOOO0OO00O000OOO .pop ()#line:74
	for O0O00000O0O00OO0O in OOOOO0OO00O000OOO :#line:76
		OO0O000O0OOO00OOO =OO0O000O0OOO00OOO +", "+O0O00000O0O00OO0O #line:77
	OO00O00OOOOO0O0OO =[]#line:79
	OO00O00OOOOO0O0OO .append (_OO0O00OO0000OOO0O .get_random_shuffle ([O000OO0O00OOO0OO0 for O000OO0O00OOO0OO0 in range (10 ,100 )if O000OO0O00OOO0OO0 %2 ==0 and O000OO0O00OOO0OO0 %3 !=0 and O000OO0O00OOO0OO0 %5 !=0 ]))#line:80
	OO00O00OOOOO0O0OO .append (_OO0O00OO0000OOO0O .get_random_shuffle ([O00OOO00OO0OOOOOO for O00OOO00OO0OOOOOO in range (10 ,100 )if O00OOO00OO0OOOOOO %2 !=0 and O00OOO00OO0OOOOOO %3 ==0 and O00OOO00OO0OOOOOO %5 !=0 ]))#line:81
	OO00O00OOOOO0O0OO .append (_OO0O00OO0000OOO0O .get_random_shuffle ([OOO0OOOOO0OO000O0 for OOO0OOOOO0OO000O0 in range (10 ,100 )if OOO0OOOOO0OO000O0 %2 !=0 and OOO0OOOOO0OO000O0 %3 !=0 and OOO0OOOOO0OO000O0 %5 ==0 ]))#line:82
	OO00O00OOOOO0O0OO .append (_OO0O00OO0000OOO0O .get_random_shuffle ([OO0O00OO000O0OOOO for OO0O00OO000O0OOOO in range (10 ,100 )if all (OO0O00OO000O0OOOO %O0000OO0O00OO0OOO !=0 for O0000OO0O00OO0OOO in range (2 ,OO0O00OO000O0OOOO ))]))#line:83
	O000O0O0O00OO0O0O =_OO0O00OO0000OOO0O .get_random_integer (0 ,2 )#line:85
	OOO0OO000O0OOOO0O =OO00O00OOOOO0O0OO .pop (O000O0O0O00OO0O0O )#line:86
	OO00O00OOOOO0O0OO =OO00O00OOOOO0O0OO [0 ]+OO00O00OOOOO0O0OO [1 ]+OO00O00OOOOO0O0OO [2 ]#line:87
	O00OO0OO000OO0000 =_OO0O00OO0000OOO0O .get_random_shuffle (list (range (0 ,6 )))[0 :4 ]#line:88
	O000OO00000O00O00 =_OO0O00OO0000OOO0O .get_random_shuffle (list (range (0 ,6 )))[0 :4 ]#line:89
	OOO0O0O000O0O000O =[]#line:91
	OOO0O0O000O0O000O .append ((4 ,1 ,True ))#line:92
	OOO0O0O000O0O000O .append ((2 ,1 ,False ))#line:93
	OOO0O0O000O0O000O .append ((3 ,2 ,False ))#line:94
	OOO0O0O000O0O000O .append ((1 ,1 ,True ))#line:95
	OOO0O0O000O0O000O .append ((2 ,3 ,False ))#line:96
	OOO0O0O000O0O000O .append ((3 ,4 ,False ))#line:97
	OOO0O0O000O0O000O .append ((1 ,4 ,True ))#line:98
	OOO0O0O000O0O000O .append ((4 ,1 ,False ))#line:99
	OOO0O0O000O0O000O .append ((1 ,3 ,True ))#line:100
	OOO0O0O000O0O000O .append ((1 ,2 ,False ))#line:101
	OOO0O0O000O0O000O .append ((1 ,1 ,False ))#line:102
	OOO0O0O000O0O000O .append ((1 ,2 ,True ))#line:103
	OOO0O0O000O0O000O .append ((1 ,2 ,True ))#line:104
	OOO0O0O000O0O000O .append ((1 ,1 ,True ))#line:105
	OOO0O00O0000O00OO =OOO0O0O000O0O000O #line:106
	_O0OO0OOOOO0O00OOO =[OOO0O00O0000O00OO .pop (OOO000O000O00OOOO )for OOO000O000O00OOOO in range (3 ,12 ,3 )]#line:107
	OOO000000O00OO0O0 =[2 ,3 ,3 ,3 ,3 ,1 ,2 ,2 ,1 ,2 ,2 ]#line:109
	OO0OOO0OO0OOO0O0O =[1 ,2 ,2 ,3 ,3 ,4 ,4 ,4 ,4 ,1 ,1 ]#line:110
	O00O0000OOOOO0OO0 =[0 ,1 ,0 ,1 ,2 ,3 ,2 ,1 ,0 ,2 ,1 ]#line:111
	OOOO0O000OOOO0OOO =open ("your-assigned-entities.dat","w")#line:113
	for O0O00000O0O00OO0O in range (24 ):#line:114
		OOOO0O000OOOO0OOO .write (str (OOO0O0O000O0O000O [O0O00000O0O00OO0O %11 ][0 ])+","+str (OOO0O0O000O0O000O [O0O00000O0O00OO0O %11 ][1 ])+"\n")#line:115
	OOOO0O000OOOO0OOO .close ()#line:116
	O000O0OO0000O0O00 =[]#line:118
	for O0O00000O0O00OO0O in range (len (OOO000000O00OO0O0 )):#line:119
		for OO00OO000O0O0O0O0 in range (OOO000000O00OO0O0 [O0O00000O0O00OO0O ]):#line:120
			O000O0OO0000O0O00 .append (str ([O00OO0OO000OO0000 [OOO0O0O000O0O000O [O0O00000O0O00OO0O ][0 ]-1 ],O000OO00000O00O00 [OOO0O0O000O0O000O [O0O00000O0O00OO0O ][1 ]-1 ],_OO0O00OO0000OOO0O .get_random_element (OOO0OO000O0OOOO0O *OOO0O0O000O0O000O [O0O00000O0O00OO0O ][2 ]+OO00O00OOOOO0O0OO *(1 -OOO0O0O000O0O000O [O0O00000O0O00OO0O ][2 ])),OO0OOO0OO0OOO0O0O [O0O00000O0O00OO0O ]-1 ]).replace (' ',''))#line:121
	OOOO0O000OOOO0OOO =open ("your-assigned-entities.dat","w")#line:123
	for O0O00000O0O00OO0O in _OO0O00OO0000OOO0O .get_random_shuffle (O000O0OO0000O0O00 ):#line:124
		OOOO0O000OOOO0OOO .write (O0O00000O0O00OO0O .strip ("[]")+"\n")#line:125
	OOOO0O000OOOO0OOO .close ()#line:126
	O0O0OO00O0OOO0O0O =["When you ran the generator it used your student number to create a file called 'your-assigned-entities.dat'. Once you have downloaded the assignment template from cuLearn, place it in the same folder as 'your-assigned-entities.dat' and 'comp1405_f17_assistant_a3.py' (a file you extracted when you extracted the generator). You must rename the assignment template to 'comp1405_f17_#########_a3.py', replacing the hashtags with your nine-digit student number.","You should test out the template by running it from the terminal by typing 'python3 comp1405_f17_#########_a3.py'. If you have done everything correctly you will see a window appear where shapes are falling from the top of the screen and disappearing when they get to the center.","Each falling shape has certain properties (such as the shape, the colour, and the numerical value) that you will be able to test (once the shape reaches the center of the screen) by calling one of the functions that has been provided. Each falling shape might also be associated with a direction (displayed as a yellow arrow under the falling shape).","Virtually all of the programming required for this assignment has already been completed for you - your ONLY task is to create the logical expressions that, once evaluated, will be assigned to the variables condition_for_sending_down, condition_for_sending_left, and condition_for_sending_right.","Each of the logical expressions you create will require that you call some of your assigned functions and use the correct logical operators (i.e., and, or, and not). As a clarifying example, if you were assigned the function 'is_the_falling_shape_red', then you could set... condition_for_sending_left = is_the_falling_shape_red(e) ...and then when you run the program, any falling shape that has the colour red will be directed to the left.","If a falling shape doesn't satisfy any of your three conditions it will disappear when it reaches the center of the screen. The shapes that do not have a yellow arrow underneath them (to indicate their target direction) should be made to disappear in this manner","Every time a falling shape is sent to its correct destination by your conditions, you will receive two points. Your score can be seen in the bottom right corner of the screen. The maximum score that is possible will be 48 (if all your shapes are each sent to their correct destinations), so if your program is able to reach that score you will know you are sorting your shapes correctly.","Please note that you can hold down the space bar to make the shapes fall more quickly while you are testing your submission.","To solve this problem you will need to run the program first and see what shapes you have been assigned (take notes!), then try to deterine what combinations of features should be sent left, right, etc. You might notice, for instance, that any shape that is a red circle or a blue triangle should be directed left.","Your conditions will not be trivial (i.e., they won't ever just require a single call to one of your assigned functions) but they should not be unneccessarily complex either.","You may use the logical operators and, or, and not to construct your conditions. You may also use any or all of the following functions: "+OO0O000O0OOO00OOO ,"WARNING: The validator does not check what functions you are using, and if you use a function you are not permitted you will receive a mark of zero even if your program works perfectly. YOUR MUST NOT USE ANY FUNCTION OTHER THAN THE ONES APPEARING IN THE LIST ABOVE!"]#line:141
	return O0O0OO00O0OOO0O0O #line:143
'''
This is the main function, primarily responsible for extracting files from the
companion archive and ensuring that the generator will actually able be able
to function with the arguments that have been provided

@params                      none
@return                      none
'''#line:153
def main ():#line:154
	clean_current_working_directory ()#line:157
	try :#line:160
		with OOO0O0O00OO0O0000 (OOO000OOOO0O0OO0O [0 ].replace ("generator","companion").replace (".py","._z"),"r")as O0000OO0OOOO000O0 :#line:161
			O0000OO0OOOO000O0 .extractall ()#line:162
	except :#line:163
		print ("")#line:164
		print ("     ┌─[ ERROR 00 ]───────────────────────────────────────────────────────┐     ")#line:165
		print ("     │                                                                    │     ")#line:166
		print ("     │ One of the files required by this generator could not be found.    │     ")#line:167
		print ("     │ When you downloaded the generator from cuLearn it was part of a    │     ")#line:168
		print ("     │ zip archive of three files - the generator, the validator, and     │     ")#line:169
		print ("     │ the companion. The generator cannot proceed because it cannot      │     ")#line:170
		print ("     │ locate the companion file. Redownload the archive from cuLearn     │     ")#line:171
		print ("     │ and then try running the generator again.                          │     ")#line:172
		print ("     │                                                                    │     ")#line:173
		print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:174
		print ("")#line:175
		exit_program ()#line:176
	import _liberr as _OO0000000O00OO000 #line:179
	import _libtui as _O0OO000OOO0O00OOO #line:180
	_O0OO000OOO0O00OOO .clear_screen ()#line:183
	print ()#line:185
	print ("     ** PLEASE NOTE:  IF YOU FAIL TO FOLLOW THESE INSTRUCTIONS PRECISELY **     ")#line:186
	print ("     **               YOUR SUBMISSION WILL RECEIVE A FINAL MARK OF ZERO. **     ")#line:187
	print ()#line:188
	O00O00O00O0OOOO0O =len (OOO000OOOO0O0OO0O )#line:191
	if O00O00O00O0OOOO0O <2 :#line:192
		_O0OO000OOO0O00OOO .print_with_a_frame (_OO0000000O00OO000 .get_error_message (_OO0000000O00OO000 .ERROR_INSUFFICIENT_ARGUMENTS ))#line:193
		exit_program ()#line:194
	O0O0000OOOO000OO0 =OOO000OOOO0O0OO0O [1 ]#line:197
	if not (O0O0000OOOO000OO0 .isdigit ()and len (O0O0000OOOO000OO0 )==9 ):#line:198
		_O0OO000OOO0O00OOO .print_with_a_frame (_OO0000000O00OO000 .get_error_message (_OO0000000O00OO000 .ERROR_INVALID_STUDENT_NUMBER ))#line:199
		exit_program ()#line:200
	O00OOO0OOO0O00OO0 =False #line:203
	for O0OOO0O00OOO0OO00 in LIST_OF_REQUISITE_FILES :#line:204
		if not O0OO000OOO0O0OO00 .exists (O0OOO0O00OOO0OO00 ):#line:205
			O00OOO0OOO0O00OO0 =True #line:206
			break #line:207
	if O00OOO0OOO0O00OO0 :#line:208
		_O0OO000OOO0O00OOO .print_with_a_frame (_OO0000000O00OO000 .get_error_message (_OO0000000O00OO000 .ERROR_REQUISITE_FILES_ABSENT ))#line:209
		exit_program ()#line:210
	OOOO00O0OO0OO0O00 =open (CURRENT_CLASS_LIST_FILE ,"r")#line:213
	OO0OOO000OOOOO00O =OOOO00O0OO0OO0O00 .read ().split ()#line:214
	OOOO00O0OO0OO0O00 .close ()#line:215
	if O0O0000OOOO000OO0 not in OO0OOO000OOOOO00O :#line:218
		_O0OO000OOO0O00OOO .print_with_a_frame (_OO0000000O00OO000 .get_error_message (_OO0000000O00OO000 .ERROR_MISSING_STUDENT_NUMBER ))#line:219
	print ("     ┌─[ OVERVIEW ]───────────────────────────────────────────────────────┐     ")#line:222
	print ("     │                                                                    │     ")#line:223
	print ("     │ For this assignment you will create a program that takes a student │     ")#line:224
	print ("     │ number from the user (submitted as a command-line variable) and    │     ")#line:225
	print ("     │ uses that data as part of a longer process. Regardless of the      │     ")#line:226
	print ("     │ student number the user submits, the process that was assigned to  │     ")#line:227
	print ("     │ your student number will always eventually produce an uppercase    │     ")#line:228
	print ("     │ letter 'A' as its final result.                                    │     ")#line:229
	print ("     │                                                                    │     ")#line:230
	print ("     │ For this assignment you will be adding exactly three conditions    │     ")#line:231
	print ("     │ (i.e., logical expressions) to the assignment template that you    │     ")#line:232
	print ("     │ will download from cuLearn in order to 'sort' a collection of      │     ")#line:233
	print ("     │ falling shapes.                                                    │     ")#line:234
	print ("     │                                                                    │     ")#line:235
	print ("     │ Your first seven lines of your submission must be a completed      │     ")#line:236
	print ("     │ copy of the following header and it must be reproduced exactly.    │     ")#line:237
	print ("     │                                                                    │     ")#line:238
	print ("     │ Check cuLearn for a sample assignment header that you may copy.    │     ")#line:239
	print ("     │                                                                    │     ")#line:240
	print ("     │ # ============================================================     │     ")#line:241
	print ("     │ #                                                                  │     ")#line:242
	print ("     │ # Student Name (as it appears on cuLearn): ????? ?????             │     ")#line:243
	print ("     │ # Student ID (9 digits in angle brackets): <?????????>             │     ")#line:244
	print ("     │ # Course Code (for this current semester): COMP1405?               │     ")#line:245
	print ("     │ #                                                                  │     ")#line:246
	print ("     │ # ============================================================     │     ")#line:247
	print ("     │                                                                    │     ")#line:248
	print ("     │ Replace the questions marks in the sample with your name,          │     ")#line:249
	print ("     │ student ID, and the letter indicating the section of COMP1405      │     ")#line:250
	print ("     │ (i.e., A or B) in which you are enrolled. Please note that the     │     ")#line:251
	print ("     │ student number must be enclosed in the angle brackets. As a        │     ")#line:252
	print ("     │ clarifying example, if your name was Robert Collier, your          │     ")#line:253
	print ("     │ student ID was 123456789, and you were enrolled in section A,      │     ")#line:254
	print ("     │ then the first seven lines of your submission must be:             │     ")#line:255
	print ("     │                                                                    │     ")#line:256
	print ("     │ # ============================================================     │     ")#line:257
	print ("     │ #                                                                  │     ")#line:258
	print ("     │ # Student Name (as it appears on cuLearn): Robert Collier          │     ")#line:259
	print ("     │ # Student ID (9 digits in angle brackets): <123456789>             │     ")#line:260
	print ("     │ # Course Code (for this current semester): COMP1405A               │     ")#line:261
	print ("     │ #                                                                  │     ")#line:262
	print ("     │ # ============================================================     │     ")#line:263
	print ("     │                                                                    │     ")#line:264
	print ("     │ Your submission must also use a specific filename in order for it  │     ")#line:265
	print ("     │ to be located by the marking utility; your submission must have    │     ")#line:266
	print ("     │ filename 'comp1405_f17_#########_a3.py', with the number signs     │     ")#line:267
	print ("     │ replaced by your nine digit student number.                        │     ")#line:268
	print ("     │                                                                    │     ")#line:269
	print ("     │ *EXCEPT* FOR RENAMING THE ASSIGNMENT TEMPLATE, CHANGING THE HEADER │     ")#line:270
	print ("     │ INFORMATION TO YOUR OWN NAME, STUDENT ID, ETC. AND WRITING LOGICAL │     ")#line:271
	print ("     │ EXPRESSIONS FOR ALL OF THE VARIABLES IN 'decision_making_function' │     ")#line:272
	print ("     │ YOU _MUST_ _NOT_ CHANGE THE TEMPLATE OR ANY OTHER FILE IN ANY WAY! │     ")#line:273
	print ("     │                                                                    │     ")#line:274
	print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:275
	OO000O0000OOO0000 =generate_assignment_instructions (O0O0000OOOO000OO0 )#line:278
	_O0OO000OOO0O00OOO .print_with_a_frame (("INSTRUCTIONS",OO000O0000OOO0000 ))#line:281
	print ()#line:283
	print ("     ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^     ")#line:284
	print ("     SCROLL UP TO THE OVERVIEW SECTION AND ENSURE YOU READ ALL INSTRUCTIONS     ")#line:285
	print ("     ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^     ")#line:286
	print ()#line:287
	exit_program ()#line:290
''' the (only) "top-level" code in the generator for calling main() '''#line:293
if __name__ =="__main__":#line:294
    main ()