from os import getcwd as O0OOO00000O0OOO0O ,listdir as OOOOOOOOOOO00OOO0 ,path as O00OO0OOO000O0000 ,remove as OOO0000O0OOOOOO00 #line:2
from sys import argv as O00O00O0OO0OO0000 #line:3
from zipfile import ZipFile as O0OOO00000OO0O00O #line:4
import textwrap as O00OO0OO0O00O0O00 #line:5
import pygame as O000O0O0000O0O0O0 #line:6
from pygame .locals import *#line:7
CURRENT_CLASS_LIST_FILE ="current_class_list.dat"#line:10
LIST_OF_REQUISITE_FILES =[CURRENT_CLASS_LIST_FILE ]+["kenpixel_mini_square.ttf"]#line:11
LIST_OF_LIBRARY_MODULES =["_liberr.py","_libtui.py","_libprg.py",]#line:16
def clean_current_working_directory ():#line:25
	OOOOOOO0OOOOO0OO0 =OOOOOOOOOOO00OOO0 (O0OOO00000O0OOO0O ())#line:27
	for OOOOO000OOO0OO0OO in OOOOOOO0OOOOO0OO0 :#line:30
		OOOOO0O0OOO0000OO =O00OO0OOO000O0000 .join (O0OOO00000O0OOO0O (),OOOOO000OOO0OO0OO )#line:33
		if not O00OO0OOO000O0000 .isdir (OOOOO0O0OOO0000OO )and (OOOOO000OOO0OO0OO in LIST_OF_REQUISITE_FILES or OOOOO000OOO0OO0OO in LIST_OF_LIBRARY_MODULES ):#line:36
			OOO0000O0OOOOOO00 (OOOOO000OOO0OO0OO )#line:38
def exit_program ():#line:47
	clean_current_working_directory ()#line:48
	exit ()#line:49
def generate_assignment_instructions (O0OOO00OOO0O0O0OO ):#line:58
	import _libprg as _OOO0OOO0OOOOOO000 #line:60
	_OOO0OOO0OOOOOO000 .set_random_source (O0OOO00OOO0O0O0OO )#line:62
	O0O00OO00O000O0OO =_OOO0OOO0OOOOOO000 .get_random_shuffle (list (range (9 )))#line:64
	O0O0OO0O0O0O0OO00 =[]#line:65
	for O0OOOOOOO0O0OOOOO in range (0 ,3 ):#line:67
		O0O0OO0O0O0O0OO00 .append ((O0O00OO00O000O0OO .pop (),"a counter-controlled 'for' loop using a call to the 'range' function"))#line:68
	O0O0OO0O0O0O0OO00 .append ((O0O00OO00O000O0OO .pop (),"a precondition, event-controlled 'while' loop using calls to the 'what_number_am_i_standing_on' function"))#line:70
	O0O0OO0O0O0O0OO00 .append ((O0O00OO00O000O0OO .pop (),"a precondition, event-controlled 'while' loop using calls to the 'am_i_standing_on' function"))#line:71
	O0O0OO0O0O0O0OO00 .append ((O0O00OO00O000O0OO .pop (),"a postcondition, event-controlled 'while' loop implemented with a 'break' statement and using calls to the 'what_number_am_i_standing_on' function"))#line:72
	O0O0OO0O0O0O0OO00 .append ((O0O00OO00O000O0OO .pop (),"a postcondition, event-controlled 'while' loop implemented with a 'break' statement and using calls to the 'am_i_standing_on' function"))#line:73
	O0O0OO0O0O0O0OO00 .append ((O0O00OO00O000O0OO .pop (),"a postcondition, event-controlled 'while' loop implemented with a Boolean flag and using calls to the 'what_number_am_i_standing_on' function"))#line:74
	O0O0OO0O0O0O0OO00 .append ((O0O00OO00O000O0OO .pop (),"a postcondition, event-controlled 'while' loop implemented with a Boolean flag and using calls to the 'am_i_standing_on' function"))#line:75
	O0O0OO0O0O0O0OO00 .sort ()#line:77
	O0000O00OO00OOO00 =65 #line:79
	OO00O0O00O0000O0O =int (O0000O00OO00OOO00 /2 )#line:80
	O00OOOOOOO0O0O000 =int (OO00O0O00O0000O0O /2 )#line:81
	O00OOO0O0OO000OOO =OO00O0O00O0000O0O +O00OOOOOOO0O0O000 #line:82
	OOO0O00000O000O00 =[[0 for O0OO00OOOOO0000OO in range (O0000O00OO00OOO00 )]for O000O0O00OO0O0OO0 in range (O0000O00OO00OOO00 )]#line:84
	OOO0OOOOOOOOOOO0O =[[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],[0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ],[0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ],[0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ],[0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ],[0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ],[0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ],[0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ],[0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ],[0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ],[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ],[0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ],[0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],[0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ],[0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ],[0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ],[0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ],[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],[0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ],[0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],[0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ],[0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],[0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ],[0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ],[0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ],[0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ],[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ],[0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ],[0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ],[0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ],[0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ],[0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ],[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ]]#line:152
	O00OO0OO00O0O0OO0 =[_OOO0OOO0OOOOOO000 .get_random_integer (0 ,14 )*2 +3 ,_OOO0OOO0OOOOOO000 .get_random_integer (0 ,14 )*2 +35 ,_OOO0OOO0OOOOOO000 .get_random_integer (0 ,14 )*2 +3 ,_OOO0OOO0OOOOOO000 .get_random_integer (0 ,14 )*2 +35 ,_OOO0OOO0OOOOOO000 .get_random_integer (0 ,14 )*2 +3 ]#line:154
	OO00000OOO00OO0O0 =[_OOO0OOO0OOOOOO000 .get_random_integer (0 ,6 )*2 +3 ,_OOO0OOO0OOOOOO000 .get_random_integer (0 ,6 )*2 +19 ,_OOO0OOO0OOOOOO000 .get_random_integer (0 ,6 )*2 +35 ,_OOO0OOO0OOOOOO000 .get_random_integer (0 ,6 )*2 +51 ,65 ]#line:155
	OO00000OO0O000000 =1 #line:157
	OOOO0O0OOO000OO0O =0 #line:158
	OO0OOO0OO00O0O000 =True #line:160
	OO0OO000OOOO00OOO =True #line:161
	O000OO0O0O0O0OOOO =O00OO0OO00O0O0OO0 [0 ]#line:163
	OO0OO0O000O0000O0 =0 #line:164
	while OO0OO0O000O0000O0 <64 :#line:166
		if OO0OOO0OO00O0O000 :#line:168
			while not OO0OO0O000O0000O0 ==OO00000OOO00OO0O0 [OOOO0O0OOO000OO0O ]:#line:169
				OOO0O00000O000O00 [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]=1 #line:170
				OO0OO0O000O0000O0 +=1 #line:171
			OOOO0O0OOO000OO0O +=1 #line:172
			OO0OOO0OO00O0O000 =not OO0OOO0OO00O0O000 #line:173
		else :#line:174
			if OO0OO000OOOO00OOO :#line:175
				while not O000OO0O0O0O0OOOO ==O00OO0OO00O0O0OO0 [OO00000OO0O000000 ]:#line:176
					OOO0O00000O000O00 [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]=1 #line:177
					O000OO0O0O0O0OOOO +=1 #line:178
			else :#line:179
				while not O000OO0O0O0O0OOOO ==O00OO0OO00O0O0OO0 [OO00000OO0O000000 ]:#line:180
					OOO0O00000O000O00 [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]=1 #line:181
					O000OO0O0O0O0OOOO -=1 #line:182
			OO00000OO0O000000 +=1 #line:183
			OO0OO000OOOO00OOO =not OO0OO000OOOO00OOO #line:184
			OO0OOO0OO00O0O000 =not OO0OOO0OO00O0O000 #line:185
	for O000OO0O0O0O0OOOO in range (len (OOO0O00000O000O00 )):#line:187
		for OO0OO0O000O0000O0 in range (len (OOO0O00000O000O00 [O000OO0O0O0O0OOOO ])):#line:188
			if OOO0O00000O000O00 [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]==1 :#line:189
				for O0OOOOOOO0O0OOOOO in range (-1 ,2 ):#line:190
					for OOO00OOO000O0O00O in range (-1 ,2 ):#line:191
						if O000OO0O0O0O0OOOO +O0OOOOOOO0O0OOOOO >=0 and O000OO0O0O0O0OOOO +O0OOOOOOO0O0OOOOO <O0000O00OO00OOO00 and OO0OO0O000O0000O0 +OOO00OOO000O0O00O >=0 and OO0OO0O000O0000O0 +OOO00OOO000O0O00O <O0000O00OO00OOO00 :#line:192
							if not OOO0O00000O000O00 [O000OO0O0O0O0OOOO +O0OOOOOOO0O0OOOOO ][OO0OO0O000O0000O0 +OOO00OOO000O0O00O ]==1 :#line:193
								OOO0O00000O000O00 [O000OO0O0O0O0OOOO +O0OOOOOOO0O0OOOOO ][OO0OO0O000O0000O0 +OOO00OOO000O0O00O ]=2 #line:194
	OO0OOO000OO0O00O0 =list (range (1 ,6 ))#line:196
	for O000OO0O0O0O0OOOO in range (len (OOO0O00000O000O00 )):#line:198
		for OO0OO0O000O0000O0 in range (len (OOO0O00000O000O00 [O000OO0O0O0O0OOOO ])):#line:199
			if OOO0OOOOOOOOOOO0O [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]==1 :#line:200
				OOO0OOOOOOOOOOO0O [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]=_OOO0OOO0OOOOOO000 .get_random_element (OO0OOO000OO0O00O0 )#line:201
	O000000O0OO00000O =_OOO0OOO0OOOOOO000 .get_random_element (OO0OOO000OO0O00O0 )#line:203
	OO0OOO000OO0O00O0 .remove (O000000O0OO00000O )#line:204
	OOO0O0OO0O0OOO00O =_OOO0OOO0OOOOOO000 .get_random_element (OO0OOO000OO0O00O0 )#line:205
	OO0OOO000OO0O00O0 .remove (OOO0O0OO0O0OOO00O )#line:206
	for O000OO0O0O0O0OOOO in range (len (OOO0O00000O000O00 )):#line:208
		for OO0OO0O000O0000O0 in range (len (OOO0O00000O000O00 [O000OO0O0O0O0OOOO ])):#line:209
			if OOO0O00000O000O00 [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]==1 :#line:210
				OOO0OOOOOOOOOOO0O [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]=_OOO0OOO0OOOOOO000 .get_random_element (OO0OOO000OO0O00O0 )#line:211
			elif OOO0O00000O000O00 [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]==2 :#line:212
				OOO0OOOOOOOOOOO0O [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]=0 #line:213
	OOO0OOOOOOOOOOO0O [O00OO0OO00O0O0OO0 [0 ]][OO00000OOO00OO0O0 [0 ]]=O000000O0OO00000O #line:215
	OOO0OOOOOOOOOOO0O [O00OO0OO00O0O0OO0 [1 ]][OO00000OOO00OO0O0 [0 ]]=OOO0O0OO0O0OOO00O #line:216
	OOO0OOOOOOOOOOO0O [O00OO0OO00O0O0OO0 [1 ]][OO00000OOO00OO0O0 [1 ]]=O000000O0OO00000O #line:217
	OOO0OOOOOOOOOOO0O [O00OO0OO00O0O0OO0 [2 ]][OO00000OOO00OO0O0 [1 ]]=OOO0O0OO0O0OOO00O #line:218
	OOO0OOOOOOOOOOO0O [O00OO0OO00O0O0OO0 [2 ]][OO00000OOO00OO0O0 [2 ]]=O000000O0OO00000O #line:219
	OOO0OOOOOOOOOOO0O [O00OO0OO00O0O0OO0 [3 ]][OO00000OOO00OO0O0 [2 ]]=OOO0O0OO0O0OOO00O #line:220
	OOO0OOOOOOOOOOO0O [O00OO0OO00O0O0OO0 [3 ]][OO00000OOO00OO0O0 [3 ]]=O000000O0OO00000O #line:221
	OOO0OOOOOOOOOOO0O [O00OO0OO00O0O0OO0 [4 ]][OO00000OOO00OO0O0 [3 ]]=OOO0O0OO0O0OOO00O #line:222
	OOO0OOOOOOOOOOO0O [O00OO0OO00O0O0OO0 [4 ]][64 ]=O000000O0OO00000O #line:223
	O00OO00O0OOO00OO0 =13 #line:225
	O0OOOO00O0OO00000 =O0000O00OO00OOO00 *O00OO00O0OOO00OO0 #line:227
	O000OOOOO0OOOOO0O =O0000O00OO00OOO00 *O00OO00O0OOO00OO0 #line:228
	O000O0O0000O0O0O0 .init ()#line:230
	O000O0O0000O0O0O0 .font .init ()#line:231
	OOO0OOOOO0O0O00OO =O000O0O0000O0O0O0 .font .Font ("kenpixel_mini_square.ttf",12 )#line:232
	O00000O0OO0OOOO00 =(64 ,64 ,64 )#line:233
	OO00OO0000OO00000 =(20 ,12 ,28 )#line:234
	OO000OOOO0OOOO000 =(222 ,238 ,214 )#line:235
	OOO000OO000O00000 =[OOO0OOOOO0O0O00OO .render (str (O0O000OOOO0O0OO00 ),True ,O00000O0OO0OOOO00 )for O0O000OOOO0O0OO00 in range (10 )]#line:236
	OOO0OOO00O00OOOO0 =O000O0O0000O0O0O0 .display .set_mode ((O0OOOO00O0OO00000 ,O000OOOOO0OOOOO0O ))#line:237
	OO00OOO0O00O0O0OO =O000O0O0000O0O0O0 .Surface ((O0OOOO00O0OO00000 ,O000OOOOO0OOOOO0O ))#line:238
	OOO0000OOOO0OOO0O =O000O0O0000O0O0O0 .Surface ((O0OOOO00O0OO00000 ,O000OOOOO0OOOOO0O ))#line:239
	OO00OOO0O00O0O0OO .fill (OO000OOOO0OOOO000 )#line:240
	for O000OO0O0O0O0OOOO in range (len (OOO0OOOOOOOOOOO0O )):#line:242
		for OO0OO0O000O0000O0 in range (len (OOO0OOOOOOOOOOO0O [O000OO0O0O0O0OOOO ])):#line:243
			if OOO0OOOOOOOOOOO0O [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]==0 :#line:245
				O000O0O0000O0O0O0 .draw .rect (OO00OOO0O00O0O0OO ,OO00OO0000OO00000 ,(O000OO0O0O0O0OOOO *O00OO00O0OOO00OO0 ,OO0OO0O000O0000O0 *O00OO00O0OOO00OO0 ,O00OO00O0OOO00OO0 ,O00OO00O0OOO00OO0 ))#line:246
			else :#line:247
				O000O0O0000O0O0O0 .draw .rect (OO00OOO0O00O0O0OO ,(OO000OOOO0OOOO000 [0 ],OO000OOOO0OOOO000 [1 ],OO000OOOO0OOOO000 [2 ]+OOO0OOOOOOOOOOO0O [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]),(O000OO0O0O0O0OOOO *O00OO00O0OOO00OO0 ,OO0OO0O000O0000O0 *O00OO00O0OOO00OO0 ,O00OO00O0OOO00OO0 ,O00OO00O0OOO00OO0 ))#line:248
			O000O0O0000O0O0O0 .draw .rect (OO00OOO0O00O0O0OO ,O00000O0OO0OOOO00 ,(O000OO0O0O0O0OOOO *O00OO00O0OOO00OO0 ,OO0OO0O000O0000O0 *O00OO00O0OOO00OO0 ,O00OO00O0OOO00OO0 ,O00OO00O0OOO00OO0 ),1 )#line:249
	OOO0OOO00O00OOOO0 .blit (OO00OOO0O00O0O0OO ,(0 ,0 ))#line:251
	for O000OO0O0O0O0OOOO in range (len (OOO0OOOOOOOOOOO0O )):#line:253
		for OO0OO0O000O0000O0 in range (len (OOO0OOOOOOOOOOO0O [O000OO0O0O0O0OOOO ])):#line:254
			if not OOO0OOOOOOOOOOO0O [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]==0 :#line:256
				OOO0OOO00O00OOOO0 .blit (OOO000OO000O00000 [OOO0OOOOOOOOOOO0O [O000OO0O0O0O0OOOO ][OO0OO0O000O0000O0 ]],(O000OO0O0O0O0OOOO *O00OO00O0OOO00OO0 +4 ,OO0OO0O000O0000O0 *O00OO00O0OOO00OO0 -1 ))#line:257
	O000O0O0000O0O0O0 .display .update ()#line:259
	O000O0O0000O0O0O0 .image .save (OOO0OOO00O00OOOO0 ,"your-assigned-maze.png")#line:260
	OOO0O0O00O00O0OO0 =["When you ran the generator it used your student number to create the image of a somewhat obvious path through a standard maze. This image was saved in a file called 'your-assigned-maze.png'. Review this image carefully. For this submission you will write a series of loops to guide a computer-controlled 'agent' along this path.","Download the assignment template from cuLearn, place it in the same folder as 'your-assigned-maze.png' and 'comp1405_f17_assistant_a5.py' (a file you extracted when you extracted the generator). You must rename the assignment template to 'comp1405_f17_#########_a5.py', replacing the hashtags with your nine-digit student number. This file is the only file you will submit for this assignment.","The template for this assignment contains a header and one essential line of code for importing functionality from the comp1405_f17_assistant_a5 module. The template also contains several function calls for moving the computer-controlled agent - these calls are only there for demonstration purposes so you must delete them as soon as you know what to expect when testing your submission.","Although you will use several different kinds of looping control structure to complete this assignment, there are only three functions you need to call to actually move through the maze. None of these functions require arguments or produces return values, and the functions themselves are named move_down, move_right, and move_left respectively.","Your path through the maze is broken into nine sections called 'legs'. The first 'leg' will start at the top row and go down. You must solve every 'leg' by using exactly one call to move_down, move_right, or move_left inside the body of the specific looping control structure assigned to that specific leg. The first 'leg' will require moving your agent down, and since a call to the move_down function will only move your agent down one unit, if you want to move your agent down a 'leg' that is five units in length then you will need to place your call to the move_down function in the body of a looping control structure that will repeat exactly five times. You must use a looping control structure for each of the nine legs of your assigned path.","You also have access to the functions 'what_number_am_i_standing_on' and 'am_i_standing_on', to be used for your event-controlled loops. The 'what_number_am_i_standing_on' function takes no arguments and returns the integer digit of the grid location where the agent is currently located, and the 'am_i_standing_on' function takes a single integer argument and returns the Boolean value (True or False) that corresponds to whether or not the agent is currently standing on a grid location with the same number as the argument.","The first 'leg' of your path starts somewhere on the top row and proceeds down. You must use exactly one "+O0O0OO0O0O0O0OO00 [0 ][1 ]+" to complete this leg of your path.","The second 'leg' of your path starts wherever the first leg ends and proceeds to the right. You must use exactly one "+O0O0OO0O0O0O0OO00 [1 ][1 ]+" to complete this leg of your path.","The third 'leg' of your path starts wherever the second leg ends and proceeds down. You must use exactly one "+O0O0OO0O0O0O0OO00 [2 ][1 ]+" to complete this leg of your path.","The fourth 'leg' of your path starts wherever the third leg ends and proceeds to the left. You must use exactly one "+O0O0OO0O0O0O0OO00 [3 ][1 ]+" to complete this leg of your path.","The fifth 'leg' of your path starts wherever the fourth leg ends and proceeds down. You must use exactly one "+O0O0OO0O0O0O0OO00 [4 ][1 ]+" to complete this leg of your path.","The sixth 'leg' of your path starts wherever the fifth leg ends and proceeds to the right. You must use exactly one "+O0O0OO0O0O0O0OO00 [5 ][1 ]+" to complete this leg of your path.","The seventh 'leg' of your path starts wherever the sixth leg ends and proceeds down. You must use exactly one "+O0O0OO0O0O0O0OO00 [6 ][1 ]+" to complete this leg of your path.","The eighth 'leg' of your path starts wherever the seventh leg ends and proceeds to the left. You must use exactly one "+O0O0OO0O0O0O0OO00 [7 ][1 ]+" to complete this leg of your path.","The ninth 'leg' of your path starts wherever the eighth leg ends and proceeds down to the bottom row (and presumably represents an escape from the maze). You must use exactly one "+O0O0OO0O0O0O0OO00 [8 ][1 ]+" to complete this leg of your path.","Do not use the input or print functions in your submission for any reason. The only functions you are permitted in this assignment are 'move_down', 'move_right', 'move_left', 'range', 'what_number_am_i_standing_on', and 'am_i_standing_on'. If your submission calls any other function you will receive a mark of zero.","The only module you are allowed to import is already imported for you (i.e., 'comp1405_f17_assistant_a5.py'). Do not make any additional imports - if you do, then you will receive a mark of zero.","When your program is running, do not change the focus away from the pygame window (i.e., do not click on another window while your program is running), as it can interfere with the ability of pygame to redraw the window.","You are expected to test your program thoroughly before submitting. Given the simplicity of the maze, and the fact that the comp1405_f17_assistant_a5 functionality will show you exactly what you are doing (whenever you test your submission), there is no reason for any student to make a submission that fails to solve the assigned maze.","If you wish to speed up the execution of your program, you may hold down the space bar.","To end this generator program, close the pygame window where your maze is currently displayed.",]#line:284
	return OOO0O0O00O00O0OO0 #line:286
def main ():#line:297
	clean_current_working_directory ()#line:300
	try :#line:303
		with O0OOO00000OO0O00O (O00O00O0OO0OO0000 [0 ].replace ("generator","companion").replace (".py","._z"),"r")as O0O0OO0O00O0000OO :#line:304
			O0O0OO0O00O0000OO .extractall ()#line:305
	except :#line:306
		print ("")#line:307
		print ("     ┌─[ ERROR 00 ]───────────────────────────────────────────────────────┐     ")#line:308
		print ("     │                                                                    │     ")#line:309
		print ("     │ One of the files required by this generator could not be found.    │     ")#line:310
		print ("     │ When you downloaded the generator from cuLearn it was part of a    │     ")#line:311
		print ("     │ zip archive of three files - the generator, the validator, and     │     ")#line:312
		print ("     │ the companion. The generator cannot proceed because it cannot      │     ")#line:313
		print ("     │ locate the companion file. Redownload the archive from cuLearn     │     ")#line:314
		print ("     │ and then try running the generator again.                          │     ")#line:315
		print ("     │                                                                    │     ")#line:316
		print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:317
		print ("")#line:318
		exit_program ()#line:319
	import _liberr as _OO0O00OO0O0OOO0OO #line:322
	import _libtui as _O00O0O0000O0OOOOO #line:323
	_O00O0O0000O0OOOOO .clear_screen ()#line:326
	print ()#line:328
	print ("     ** PLEASE NOTE:  IF YOU FAIL TO FOLLOW THESE INSTRUCTIONS PRECISELY **     ")#line:329
	print ("     **               YOUR SUBMISSION WILL RECEIVE A FINAL MARK OF ZERO. **     ")#line:330
	print ()#line:331
	O0OOOO0OOO0O000OO =len (O00O00O0OO0OO0000 )#line:334
	if O0OOOO0OOO0O000OO <2 :#line:335
		_O00O0O0000O0OOOOO .print_with_a_frame (_OO0O00OO0O0OOO0OO .get_error_message (_OO0O00OO0O0OOO0OO .ERROR_INSUFFICIENT_ARGUMENTS ))#line:336
		exit_program ()#line:337
	O0000OOOOO000OOO0 =O00O00O0OO0OO0000 [1 ]#line:340
	if not (O0000OOOOO000OOO0 .isdigit ()and len (O0000OOOOO000OOO0 )==9 ):#line:341
		_O00O0O0000O0OOOOO .print_with_a_frame (_OO0O00OO0O0OOO0OO .get_error_message (_OO0O00OO0O0OOO0OO .ERROR_INVALID_STUDENT_NUMBER ))#line:342
		exit_program ()#line:343
	O000OOOO0O00OO00O =False #line:346
	for O00O0O0O0OO00O000 in LIST_OF_REQUISITE_FILES :#line:347
		if not O00OO0OOO000O0000 .exists (O00O0O0O0OO00O000 ):#line:348
			O000OOOO0O00OO00O =True #line:349
			break #line:350
	if O000OOOO0O00OO00O :#line:351
		_O00O0O0000O0OOOOO .print_with_a_frame (_OO0O00OO0O0OOO0OO .get_error_message (_OO0O00OO0O0OOO0OO .ERROR_REQUISITE_FILES_ABSENT ))#line:352
		exit_program ()#line:353
	OOOO0O0OOO0OOOO00 =open (CURRENT_CLASS_LIST_FILE ,"r")#line:356
	OO00OO0OOO000O00O =OOOO0O0OOO0OOOO00 .read ().split ()#line:357
	OOOO0O0OOO0OOOO00 .close ()#line:358
	if O0000OOOOO000OOO0 not in OO00OO0OOO000O00O :#line:361
		_O00O0O0000O0OOOOO .print_with_a_frame (_OO0O00OO0O0OOO0OO .get_error_message (_OO0O00OO0O0OOO0OO .ERROR_MISSING_STUDENT_NUMBER ))#line:362
	print ("     ┌─[ OVERVIEW ]───────────────────────────────────────────────────────┐     ")#line:365
	print ("     │                                                                    │     ")#line:366
	print ("     │ For this assignment you will create a program that uses looping    │     ")#line:367
	print ("     │ control structures to guide a computer-controlled agent along a    │     ")#line:368
	print ("     │ specific (but incredibly obvious) path through a simple maze, from │     ")#line:369
	print ("     │ a starting point on the top row to an ending point on the bottom.  │     ")#line:370
	print ("     │                                                                    │     ")#line:371
	print ("     │ The path will always be broken into nine sections known as 'legs'. │     ")#line:372
	print ("     │ The first 'leg' will start at the top and proceed down, the second │     ")#line:373
	print ("     │ will continue from there and proceed either left or right, etc.    │     ")#line:374
	print ("     │                                                                    │     ")#line:375
	print ("     │ Because each 'leg' will require you to move down, left, or right   │     ")#line:376
	print ("     │ a certain number of times, you will write a single looping control │     ")#line:377
	print ("     │ structure to handle each of the nine 'legs'. The specific details  │     ")#line:378
	print ("     │ about the control structures you must create for each 'leg' are    │     ")#line:379
	print ("     │ described in greater detail below.                                 │     ")#line:380
	print ("     │                                                                    │     ")#line:381
	print ("     │ Your first seven lines of your submission must be a completed      │     ")#line:382
	print ("     │ copy of the following header and it must be reproduced exactly.    │     ")#line:383
	print ("     │                                                                    │     ")#line:384
	print ("     │ Check cuLearn for a sample assignment header that you may copy.    │     ")#line:385
	print ("     │                                                                    │     ")#line:386
	print ("     │ # ============================================================     │     ")#line:387
	print ("     │ #                                                                  │     ")#line:388
	print ("     │ # Student Name (as it appears on cuLearn): ????? ?????             │     ")#line:389
	print ("     │ # Student ID (9 digits in angle brackets): <?????????>             │     ")#line:390
	print ("     │ # Course Code (for this current semester): COMP1405?               │     ")#line:391
	print ("     │ #                                                                  │     ")#line:392
	print ("     │ # ============================================================     │     ")#line:393
	print ("     │                                                                    │     ")#line:394
	print ("     │ Replace the questions marks in the sample with your name,          │     ")#line:395
	print ("     │ student ID, and the letter indicating the section of COMP1405      │     ")#line:396
	print ("     │ (i.e., A or B) in which you are enrolled. Please note that the     │     ")#line:397
	print ("     │ student number must be enclosed in the angle brackets. As a        │     ")#line:398
	print ("     │ clarifying example, if your name was Robert Collier, your          │     ")#line:399
	print ("     │ student ID was 123456789, and you were enrolled in section A,      │     ")#line:400
	print ("     │ then the first seven lines of your submission must be:             │     ")#line:401
	print ("     │                                                                    │     ")#line:402
	print ("     │ # ============================================================     │     ")#line:403
	print ("     │ #                                                                  │     ")#line:404
	print ("     │ # Student Name (as it appears on cuLearn): Robert Collier          │     ")#line:405
	print ("     │ # Student ID (9 digits in angle brackets): <123456789>             │     ")#line:406
	print ("     │ # Course Code (for this current semester): COMP1405A               │     ")#line:407
	print ("     │ #                                                                  │     ")#line:408
	print ("     │ # ============================================================     │     ")#line:409
	print ("     │                                                                    │     ")#line:410
	print ("     │ Your submission must also use a specific filename in order for it  │     ")#line:411
	print ("     │ to be located by the marking utility; your submission must have    │     ")#line:412
	print ("     │ filename 'comp1405_f17_#########_a5.py', with the number signs     │     ")#line:413
	print ("     │ replaced by your nine digit student number.                        │     ")#line:414
	print ("     │                                                                    │     ")#line:415
	print ("     └────────────────────────────────────────────────────────────────────┘     ")#line:416
	O0OO0OO0OO0O00OOO =generate_assignment_instructions (O0000OOOOO000OOO0 )#line:419
	_O00O0O0000O0OOOOO .print_with_a_frame (("INSTRUCTIONS",O0OO0OO0OO0O00OOO ))#line:422
	print ()#line:424
	print ("     ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^     ")#line:425
	print ("     SCROLL UP TO THE OVERVIEW SECTION AND ENSURE YOU READ ALL INSTRUCTIONS     ")#line:426
	print ("     ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^     ")#line:427
	print ()#line:428
	O00O000000O0O0O00 =False #line:430
	while not O00O000000O0O0O00 :#line:431
		for O0OOOO00O0O00O0O0 in O000O0O0000O0O0O0 .event .get ():#line:432
			if O0OOOO00O0O00O0O0 .type ==QUIT :#line:433
				O00O000000O0O0O00 =True #line:434
	exit_program ()#line:437
if __name__ =="__main__":#line:441
    main ()
