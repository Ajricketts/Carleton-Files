from os import getcwd as OO00O0000OOOO0O0O ,listdir as OO0OOOO000OOOOO0O ,path as O0OOOOOO0O0OO0OO0 ,remove as OOOOOO0O00O0O0000 #line:2
from sys import argv as OO0OO0OOOO000000O #line:3
from zipfile import ZipFile as OOOO0O00000O0OO0O #line:4
import textwrap as O0O000OOO0000O00O #line:5
import pygame as O0OO0O00O000OO000 #line:6
from pygame .locals import *#line:7
CURRENT_CLASS_LIST_FILE ="current_class_list.dat"#line:10
LIST_OF_REQUISITE_FILES =[CURRENT_CLASS_LIST_FILE ]+["guesswho_earring.png","guesswho_eyepatch.png","guesswho_face.png","guesswho_glasses.png","guesswho_hair.png","guesswho_hat.png","guesswho_moustache.png","guesswho_pipe.png","guesswho_tattoo.png","guesswho_tie.png"]#line:11
LIST_OF_LIBRARY_MODULES =["_liberr.py","_libtui.py","_libprg.py",]#line:16
'''
This will remove all the files that were extracted from the companion

@params                      none
@return                      none
'''#line:24
def clean_current_working_directory ():#line:25
	OOO0OOO0O0OO0OO0O =OO0OOOO000OOOOO0O (OO00O0000OOOO0O0O ())#line:27
	for OO0O0O0OO0OO0O000 in OOO0OOO0O0OO0OO0O :#line:30
		O000OOO0O00OOO0O0 =O0OOOOOO0O0OO0OO0 .join (OO00O0000OOOO0O0O (),OO0O0O0OO0OO0O000 )#line:33
		if not O0OOOOOO0O0OO0OO0 .isdir (O000OOO0O00OOO0O0 )and (OO0O0O0OO0OO0O000 in LIST_OF_REQUISITE_FILES or OO0O0O0OO0OO0O000 in LIST_OF_LIBRARY_MODULES ):#line:36
			OOOOOO0O00O0O0000 (OO0O0O0OO0OO0O000 )#line:38
'''
This is end the program after cleaning the current working directory

@params                      none
@return                      none
'''#line:46
def exit_program ():#line:47
	clean_current_working_directory ()#line:48
	exit ()#line:49
'''
This is the actual instruction generator that is specific to this assignment

@params                      none
@return                      none
'''#line:57
def generate_assignment_instructions (OOO00OO0O00OO0OOO ):#line:58
	import _libprg as _O00OOOO000O0O0OOO #line:60
	_O00OOOO000O0O0OOO .set_random_source (OOO00OO0O00OO0OOO )#line:62
	O00O0O00000OO0000 =16 #line:64
	O0OOO0OO0OO00O0OO =["Addison","Adrian","Aiden","Ainsley","Alex","Amari","Andy","Ari","Ash","Aspen","Aubrey","August","Avery","Bailey","Bay","Blaine","Blake","Bobbie","Brett","Brook","Brooklyn","Caelan","Cameron","Campbell","Carroll","Carson","Casey","Charlie","Chris","Clay","Corey","Dana","Dakota","Dale","Dallas","Daryl","Delta","Devin","Dorian","Drew","Dylan","Easton","Eddie","Eli","Elliott","Emerson","Emery","Finley","Frances","Frankie","Gabriel","Glenn","Gray","Harley","Harper","Hayden","Hudson","Hunter","James","Jamie","Jayden","Jean","Jesse","Jordan","Jules","Julian","Kaden","Kai","Karter","Kelly","Kelsey","Kendall","Kennedy","Kyle","Lake","Landry","Lincoln","Logan","London","Lou","Mackenzie","Mason","Max","Maxwell","Monroe","Morgan","Parker","Pat","Peyton","Phoenix","Quinn","Ray","Reagan","Reed","Reese","Remy","Riley","River","Roan","Rory","Rowan","Rudy","Ryan","Sage","Sam","Sawyer","Shawn","Sean","Skylar","Spencer","Stevie","Sydney","Tanner","Tatum","Taylor","Toby","Tyler","Val","West","Winter"]#line:66
	OOO00O00O0OOOOOOO =[]#line:68
	for O000OO0OO0OO00O0O in range (O00O0O00000OO0000 ):#line:69
		OOO00O00O0OOOOOOO .append (O0OOO0OO0OO00O0OO .pop (_O00OOOO000O0O0OOO .get_random_integer (0 ,len (O0OOO0OO0OO00O0OO )-1 )))#line:70
	O00O0O00000OOOOO0 =[64 ,120 ,4 ,56 ,8 ,4 ,108 ,16 ,4 ,92 ,32 ]#line:72
	O000OO0O0OOOO00OO =[0 ]#line:73
	for O000OO0OO0OO00O0O in O00O0O00000OOOOO0 :#line:74
		O000OO0O0OOOO00OO .insert (0 ,O000OO0O0OOOO00OO [0 ]+O000OO0OO0OO00O0O )#line:75
	O00O00OO000000000 =[508 ,380 ,252 ,188 ]#line:77
	for O000OO0OO0OO00O0O in O00O00OO000000000 :#line:79
		O000OO0O0OOOO00OO .append (O000OO0OO0OO00O0O +_O00OOOO000O0O0OOO .get_random_integer (1 ,3 ))#line:80
	O000OO0O0OOOO00OO =_O00OOOO000O0O0OOO .get_random_shuffle (O000OO0O0OOOO00OO )#line:82
	O0OO0O00O000OO000 .init ()#line:84
	O00O0O0O0O0OO0OOO =O0OO0O00O000OO000 .font .SysFont ("monospace",18 ,bold =True )#line:86
	(OOO0000OO00O00000 ,OOO0O000O0000OO0O )=(150 ,175 )#line:88
	O0O00OO0OO00000OO =O0OO0O00O000OO000 .display .set_mode ((OOO0000OO00O00000 *4 ,OOO0O000O0000OO0O *4 ))#line:90
	O0O00OO0OO00000OO .fill ((255 ,255 ,255 ))#line:91
	OOO0OO0OOO0000OO0 =[]#line:93
	OOO0OO0OOO0000OO0 .append ('guesswho_earring.png')#line:94
	OOO0OO0OOO0000OO0 .append ('guesswho_eyepatch.png')#line:95
	OOO0OO0OOO0000OO0 .append ('guesswho_glasses.png')#line:96
	OOO0OO0OOO0000OO0 .append ('guesswho_hair.png')#line:97
	OOO0OO0OOO0000OO0 .append ('guesswho_hat.png')#line:98
	OOO0OO0OOO0000OO0 .append ('guesswho_moustache.png')#line:99
	OOO0OO0OOO0000OO0 .append ('guesswho_pipe.png')#line:100
	OOO0OO0OOO0000OO0 .append ('guesswho_tattoo.png')#line:101
	OOO0OO0OOO0000OO0 .append ('guesswho_tie.png')#line:102
	OOO0OO0OOO0000OO0 =_O00OOOO000O0O0OOO .get_random_shuffle (OOO0OO0OOO0000OO0 )#line:104
	OO000000O000O0OOO =[]#line:106
	for O000OO0OO0OO00O0O in OOO0OO0OOO0000OO0 :#line:107
		OO000000O000O0OOO .append (O0OO0O00O000OO000 .image .load (O000OO0OO0OO00O0O ).convert_alpha ())#line:108
	O0O00OOOO00OO0OOO =O0OO0O00O000OO000 .image .load ('guesswho_face.png')#line:110
	OO000000O000O0OOO =OO000000O000O0OOO [0 :9 ]#line:112
	for O000OO0OO0OO00O0O in range (O00O0O00000OO0000 ):#line:114
		OOOOOOO0000O00O0O =O00O0O0O0O0OO0OOO .render (OOO00O00O0OOOOOOO [O000OO0OO0OO00O0O ],1 ,(0 ,0 ,0 ))#line:115
		OOO000O0O0OOO0O0O ,O0O00O000OOO00O00 =O00O0O0O0O0OO0OOO .size (OOO00O00O0OOOOOOO [O000OO0OO0OO00O0O ])#line:116
		O00O0000OOO0O0000 =OOO000O0O0OOO0O0O //2 #line:117
		OO0OO00000O00OO00 =O0O00O000OOO00O00 //2 #line:118
		(O0O0OO0OOOO000000 ,O0OOOO000000OO00O )=((O000OO0OO0OO00O0O %4 )*OOO0000OO00O00000 ,(O000OO0OO0OO00O0O //4 )*OOO0O000O0000OO0O )#line:119
		O0O00OO0OO00000OO .blit (O0O00OOOO00OO0OOO ,(O0O0OO0OOOO000000 ,O0OOOO000000OO00O ))#line:120
		O0O00OO0OO00000OO .blit (OOOOOOO0000O00O0O ,(O0O0OO0OOOO000000 +OOO0000OO00O00000 /2 -O00O0000OOO0O0000 ,O0OOOO000000OO00O +OOO0O000O0000OO0O -25 -OO0OO00000O00OO00 ))#line:121
		for OOO0OOOO0O0O00O00 in range (0 ,9 ):#line:122
			if int (bin (O000OO0O0OOOO00OO [O000OO0OO0OO00O0O ])[2 :].zfill (9 )[OOO0OOOO0O0O00O00 ]):#line:123
				O0O00OO0OO00000OO .blit (OO000000O000O0OOO [OOO0OOOO0O0O00O00 ],(O0O0OO0OOOO000000 ,O0OOOO000000OO00O ))#line:124
	O0OO0O00O000OO000 .display .update ()#line:126
	O0OO0O00O000OO000 .image .save (O0O00OO0OO00000OO ,"your-game-board.png")#line:127
	OOOOO00OO00OO0000 =["When you ran the generator it used your student number to create a collection of faces and an image of the game board of faces for playing the game. This image was saved in a file called 'your-game-board.png'. Review this image carefully because the branching control structures you develop for this submission will reference the features in the faces of this image, but please note that you are not including this file with your submission.","Download the assignment template from cuLearn, place it in the same folder as 'your-game-board.png' and 'comp1405_f17_assistant_a4.py' (a file you extracted when you extracted the generator). You must rename the assignment template to 'comp1405_f17_#########_a4.py', replacing the hashtags with your nine-digit student number. This file is the only file you will submit.","The template for this assignment contains only a header and one line of code. The 'from comp1405_f17_assistant_a4 import *' instruction will give you access to two functions provided in the 'comp1405_f17_assistant_a4.py' module. See the next item for more details.","You cannot use the print function or the input function when completing this assignment. Instead, in order for your program to interact with the player, you must use the ask_question and make_a_guess functions that were imported from the 'comp1405_f17_assistant_a4.py' module. The ask_question function takes a single string argument and returns a string; the argument is the question that the computer wishes to ask and the return value string is the response entered by the player. The make_a_guess function takes a single string argument and has no return value; the argument is what the computer has concluded about the identity of the player. Review these functions carefully but do not modify them in any way. Pay careful attention to the possible values that could be returned by the ask_question function.","Please note that for this variant the computer program is only allowed to guess at the identity of the player once. In other words, the computer program must be 100% certain about the identity of the player before calling the make_a_guess function. The computer program must also be able to identify the human player in less than five guesses - if you review the features of your assigned faces carefully, you should have no difficulty coming up with the collection of questions the computer should ask. In many ways, the submission you are preparing for this assignment is very similar to the dichotomous key example that was discussed in class.","In order for your submission to receive a mark, each of the string arguments you provide to the ask_question function must contain one and only one of the following words: ['earring', 'eyepatch', 'glasses', 'hair', 'hat', 'moustache', 'pipe', 'tattoo', 'tie']. The case does not matter, but exactly one of these words must appear in your question, as these are the only features that can be used to uniquely identify one of the cartoon faces. As a clarifying example, the string 'Are you wearing a hat?' would be a valid question, but the string 'Does your name start with the letter A?' would be an invalid question. If your submission uses any invalid questions you will receive a mark of zero.","Similarly, each of the string arguments you provide to the make_a_guess function must contain one and only one of the names that appears on your game board. Once again, although the case does not matter, if any of your calls to the make_a_guess function are passed an argument that does not contain one (and only one) of the names that you have been assigned, your submission will receive a mark of zero.","Do not use the input or print functions in your submission. The only functions you are permitted in this assignment are upper, lower, ask_question, and make_a_guess. If your submission calls any other function you will receive a mark of zero.","The only module you are allowed to import is already imported for you (i.e., 'comp1405_f17_assistant_a4.py'). Do not make any additional imports - if you do, then you will receive a mark of zero.","Close the pygame window to terminate this generator."]#line:139
	return OOOOO00OO00OO0000 #line:141
'''
This is the main function, primarily responsible for extracting files from the
companion archive and ensuring that the generator will actually able be able
to function with the arguments that have been provided

@params                      none
@return                      none
'''#line:151
def main ():#line:152
	clean_current_working_directory ()#line:155
	try :#line:158
		with OOOO0O00000O0OO0O (OO0OO0OOOO000000O [0 ].replace ("generator","companion").replace (".py","._z"),"r")as OOO0000OOO0OO00OO :#line:159
			OOO0000OOO0OO00OO .extractall ()#line:160
	except :#line:161
		print ("")#line:162
		print ("     ┌─[ ERROR 00 ]───────────────────────────────────────────────────────┐     ")#line:163
		print ("     │                                                                    │     ")#line:164
		print ("     │ One of the files required by this generator could not be found.    │     ")#line:165
		print ("     │ When you downloaded the generator from cuLearn it was part of a    │     ")#line:166
		print ("     │ zip archive of three files - the generator, the validator, and     │     ")#line:167
		print ("     │ the companion. The generator cannot proceed because it cannot      │     ")#line:168
		print ("     │ locate the companion file. Redownload the archive from cuLearn     │     ")#line:169
		print ("     │ and then try running the generator again.                          │     ")#line:170
		print ("     │                                                                    │     ")#line:171
		print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:172
		print ("")#line:173
		exit_program ()#line:174
	import _liberr as _OO000000O0OOOO0O0 #line:177
	import _libtui as _OO0O00O0000000O0O #line:178
	_OO0O00O0000000O0O .clear_screen ()#line:181
	print ()#line:183
	print ("     ** PLEASE NOTE:  IF YOU FAIL TO FOLLOW THESE INSTRUCTIONS PRECISELY **     ")#line:184
	print ("     **               YOUR SUBMISSION WILL RECEIVE A FINAL MARK OF ZERO. **     ")#line:185
	print ()#line:186
	O0000O0000O00OO0O =len (OO0OO0OOOO000000O )#line:189
	if O0000O0000O00OO0O <2 :#line:190
		_OO0O00O0000000O0O .print_with_a_frame (_OO000000O0OOOO0O0 .get_error_message (_OO000000O0OOOO0O0 .ERROR_INSUFFICIENT_ARGUMENTS ))#line:191
		exit_program ()#line:192
	O00000O0O00OOO0O0 =OO0OO0OOOO000000O [1 ]#line:195
	if not (O00000O0O00OOO0O0 .isdigit ()and len (O00000O0O00OOO0O0 )==9 ):#line:196
		_OO0O00O0000000O0O .print_with_a_frame (_OO000000O0OOOO0O0 .get_error_message (_OO000000O0OOOO0O0 .ERROR_INVALID_STUDENT_NUMBER ))#line:197
		exit_program ()#line:198
	O0000OOOO0O0OOO00 =False #line:201
	for OO0O00OOO0000OOOO in LIST_OF_REQUISITE_FILES :#line:202
		if not O0OOOOOO0O0OO0OO0 .exists (OO0O00OOO0000OOOO ):#line:203
			O0000OOOO0O0OOO00 =True #line:204
			break #line:205
	if O0000OOOO0O0OOO00 :#line:206
		_OO0O00O0000000O0O .print_with_a_frame (_OO000000O0OOOO0O0 .get_error_message (_OO000000O0OOOO0O0 .ERROR_REQUISITE_FILES_ABSENT ))#line:207
		exit_program ()#line:208
	OO0O0OO0O00O0OOO0 =open (CURRENT_CLASS_LIST_FILE ,"r")#line:211
	O0O0O0O00O00O0O00 =OO0O0OO0O00O0OOO0 .read ().split ()#line:212
	OO0O0OO0O00O0OOO0 .close ()#line:213
	if O00000O0O00OOO0O0 not in O0O0O0O00O00O0O00 :#line:216
		_OO0O00O0000000O0O .print_with_a_frame (_OO000000O0OOOO0O0 .get_error_message (_OO000000O0OOOO0O0 .ERROR_MISSING_STUDENT_NUMBER ))#line:217
	print ("     ┌─[ OVERVIEW ]───────────────────────────────────────────────────────┐     ")#line:220
	print ("     │                                                                    │     ")#line:221
	print ("     │ For this assignment you will create a program that plays a one     │     ")#line:222
	print ("     │ person variant of the game 'Guess Who'. If you have never played   │     ")#line:223
	print ("     │ this game before then you must read about it at:                   │     ")#line:224
	print ("     │ https://en.wikipedia.org/wiki/Guess_Who%3F.                        │     ")#line:225
	print ("     │                                                                    │     ")#line:226
	print ("     │ The game you are creating is played between one human player and   │     ")#line:227
	print ("     │ your computer program. The human player will look at a collection  │     ")#line:228
	print ("     │ of 16 cartoon faces and select one - this will be that player's    │     ")#line:229
	print ("     │ identity. The computer program will then ask the player some yes   │     ")#line:230
	print ("     │ or no questions about the features of their chosen identity, and   │     ")#line:231
	print ("     │ the human player must answer truthfully. Eventually the computer   │     ")#line:232
	print ("     │ program should have enough information to identify which of the 16 │     ")#line:233
	print ("     │ faces was selected by the player and at that point the game is     │     ")#line:234
	print ("     │ over.                                                              │     ")#line:235
	print ("     │                                                                    │     ")#line:236
	print ("     │ Your submission will be structurally similar to the second of the  │     ")#line:237
	print ("     │ dichotomous key examples presented in class, so you must review    │     ")#line:238
	print ("     │ those examples before you begin.                                   │     ")#line:239
	print ("     │                                                                    │     ")#line:240
	print ("     │ Your first seven lines of your submission must be a completed      │     ")#line:241
	print ("     │ copy of the following header and it must be reproduced exactly.    │     ")#line:242
	print ("     │                                                                    │     ")#line:243
	print ("     │ Check cuLearn for a sample assignment header that you may copy.    │     ")#line:244
	print ("     │                                                                    │     ")#line:245
	print ("     │ # ============================================================     │     ")#line:246
	print ("     │ #                                                                  │     ")#line:247
	print ("     │ # Student Name (as it appears on cuLearn): ????? ?????             │     ")#line:248
	print ("     │ # Student ID (9 digits in angle brackets): <?????????>             │     ")#line:249
	print ("     │ # Course Code (for this current semester): COMP1405?               │     ")#line:250
	print ("     │ #                                                                  │     ")#line:251
	print ("     │ # ============================================================     │     ")#line:252
	print ("     │                                                                    │     ")#line:253
	print ("     │ Replace the questions marks in the sample with your name,          │     ")#line:254
	print ("     │ student ID, and the letter indicating the section of COMP1405      │     ")#line:255
	print ("     │ (i.e., A or B) in which you are enrolled. Please note that the     │     ")#line:256
	print ("     │ student number must be enclosed in the angle brackets. As a        │     ")#line:257
	print ("     │ clarifying example, if your name was Robert Collier, your          │     ")#line:258
	print ("     │ student ID was 123456789, and you were enrolled in section A,      │     ")#line:259
	print ("     │ then the first seven lines of your submission must be:             │     ")#line:260
	print ("     │                                                                    │     ")#line:261
	print ("     │ # ============================================================     │     ")#line:262
	print ("     │ #                                                                  │     ")#line:263
	print ("     │ # Student Name (as it appears on cuLearn): Robert Collier          │     ")#line:264
	print ("     │ # Student ID (9 digits in angle brackets): <123456789>             │     ")#line:265
	print ("     │ # Course Code (for this current semester): COMP1405A               │     ")#line:266
	print ("     │ #                                                                  │     ")#line:267
	print ("     │ # ============================================================     │     ")#line:268
	print ("     │                                                                    │     ")#line:269
	print ("     │ Your submission must also use a specific filename in order for it  │     ")#line:270
	print ("     │ to be located by the marking utility; your submission must have    │     ")#line:271
	print ("     │ filename 'comp1405_f17_#########_a4.py', with the number signs     │     ")#line:272
	print ("     │ replaced by your nine digit student number.                        │     ")#line:273
	print ("     │                                                                    │     ")#line:274
	print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:275
	OO0O0000OO000OO0O =generate_assignment_instructions (O00000O0O00OOO0O0 )#line:278
	_OO0O00O0000000O0O .print_with_a_frame (("INSTRUCTIONS",OO0O0000OO000OO0O ))#line:281
	print ()#line:283
	print ("     ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^     ")#line:284
	print ("     SCROLL UP TO THE OVERVIEW SECTION AND ENSURE YOU READ ALL INSTRUCTIONS     ")#line:285
	print ("     ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^     ")#line:286
	print ()#line:287
	OO00O000OO0O0O0OO =False #line:289
	while not OO00O000OO0O0O0OO :#line:290
		for OO0O00O000OOO0O0O in O0OO0O00O000OO000 .event .get ():#line:291
			if OO0O00O000OOO0O0O .type ==QUIT :#line:292
				OO00O000OO0O0O0OO =True #line:293
	exit_program ()#line:296
''' the (only) "top-level" code in the generator for calling main() '''#line:299
if __name__ =="__main__":#line:300
    main ()
#e9015584e6a44b14988f13e2298bcbf9


#===============================================================#
# Obfuscated by Oxyry Python Obfuscator (http://pyob.oxyry.com) #
#===============================================================#
