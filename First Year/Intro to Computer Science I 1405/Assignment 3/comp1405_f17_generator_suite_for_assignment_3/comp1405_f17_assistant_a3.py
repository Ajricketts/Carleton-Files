import pygame as O0OOO0000O0OO0O00 #line:1
O0OOO0000O0OO0O00 .init ()#line:3
l11llll1ll ={}#line:5
l11llll1ll [0 ]=(192 ,0 ,0 )#line:6
l11llll1ll [1 ]=(215 ,98 ,19 )#line:7
l11llll1ll [2 ]=(0 ,176 ,80 )#line:8
l11llll1ll [3 ]=(0 ,112 ,192 )#line:9
l11llll1ll [4 ]=(112 ,48 ,160 )#line:10
l11llll1ll [5 ]=(0 ,0 ,0 )#line:11
lll1l1l11l ={}#line:13
lll1l1l11l [0 ]="o"#line:14
lll1l1l11l [1 ]="s"#line:15
lll1l1l11l [2 ]="d"#line:16
lll1l1l11l [3 ]="c"#line:17
lll1l1l11l [4 ]="t"#line:18
lll1l1l11l [5 ]="p"#line:19
l1lllll11l ={}#line:21
l1lllll11l [0 ]="L"#line:22
l1lllll11l [1 ]="R"#line:23
l1lllll11l [2 ]="D"#line:24
l1lllll11l [3 ]="X"#line:25
window_side =600 #line:27
window_half =window_side //2 #line:28
window =O0OOO0000O0OO0O00 .display .set_mode ((window_side ,window_side ))#line:30
entity_side =30 #line:32
entity_half =entity_side //2 #line:33
font =O0OOO0000O0OO0O00 .font .SysFont ("monospace",18 ,bold =True )#line:35
font_wide ,font_high =font .size ("88")#line:37
font_half_wide =font_wide //2 #line:38
font_half_high =font_high //2 #line:39
def run_the_program (OO00OO000OO000OOO ):#line:42
	OO0O0O0O0O0OOO0O0 =0 #line:44
	O0OOO000OO0O0OO0O =open ("your-assigned-entities.dat","r")#line:46
	O000O000O00O0OOOO =O0OOO000OO0O0OO0O .read ().strip ('\n').split ('\n')#line:47
	O0OOO000OO0O0OO0O .close ()#line:48
	OO0OOOO000OO0OO00 =[]#line:49
	OOO0OOO0OO00O0O00 =0 #line:50
	for OOOO00000OOOOOOO0 in O000O000O00O0OOOO :#line:51
		(O0000O00O000O0O00 ,OO00O00OOOO000O0O ,OO00O0O0OO000OO0O ,OO00OO00OO0OOOO00 )=tuple (OOOO00000OOOOOOO0 .split (','))#line:52
		OO0OOOO000OO0OO00 .append (Entity (O0000O00O000O0O00 ,OO00O00OOOO000O0O ,OO00O0O0OO000OO0O ,OOO0OOO0OO00O0O00 ,OO00OO00OO0OOOO00 ))#line:53
		OOO0OOO0OO00O0O00 +=200 #line:54
	while len (OO0OOOO000OO0OO00 )>0 :#line:56
		window .fill ((64 ,64 ,64 ))#line:58
		for OOO0O00OO0OOOOO0O in range (len (OO0OOOO000OO0OO00 )-1 ,-1 ,-1 ):#line:60
			if OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].delay >0 :#line:61
				OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].delay -=1 #line:62
			elif OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].y <window_half :#line:63
				OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].y +=1 #line:64
				OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].draw ()#line:65
			elif OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].y ==window_half :#line:66
				OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].y +=1 #line:68
				(OOOO00O00OOO000O0 ,O0OOOO00OOOOO00OO ,O00O00O0O000O000O )=OO00OO000OO000OOO (OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ])#line:70
				if OOOO00O00OOO000O0 :#line:72
					OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].direction ="D"#line:73
				elif O0OOOO00OOOOO00OO :#line:74
					OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].direction ="L"#line:75
				elif O00O00O0O000O000O :#line:76
					OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].direction ="R"#line:77
				else :#line:78
					if OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].target_edge ==3 :#line:80
						OO0O0O0O0O0OOO0O0 +=2 #line:81
					OO0OOOO000OO0OO00 .pop (OOO0O00OO0OOOOO0O )#line:83
			else :#line:85
				if OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].direction =="L":#line:87
					OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].x -=1 #line:88
				elif OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].direction =="R":#line:89
					OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].x +=1 #line:90
				else :#line:91
					OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].y +=1 #line:92
				OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].draw ()#line:94
				if OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].y -font_half_high >window_side or OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].x -font_half_wide >window_side or OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].x +font_half_wide <1 :#line:96
					if OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].direction ==l1lllll11l [OO0OOOO000OO0OO00 [OOO0O00OO0OOOOO0O ].target_edge ]:#line:98
						OO0O0O0O0O0OOO0O0 +=2 #line:99
					OO0OOOO000OO0OO00 .pop (OOO0O00OO0OOOOO0O )#line:101
		OOO0OO0O00O00000O =font .render (str (OO0O0O0O0O0OOO0O0 ),1 ,(255 ,255 ,0 ))#line:103
		O00OO0OO0O0OOO0O0 ,O0000O0O00000O0OO =font .size (str (OO0O0O0O0O0OOO0O0 ))#line:104
		window .blit (OOO0OO0O00O00000O ,(window_side -O00OO0OO0O0OOO0O0 ,window_side -O0000O0O00000O0OO ))#line:105
		O0OOO0000O0OO0O00 .display .update ()#line:106
		if (O0OOO0000O0OO0O00 .key .get_pressed ()[O0OOO0000O0OO0O00 .K_SPACE ]==0 ):#line:108
			O0OOO0000O0OO0O00 .time .delay (6 )#line:109
		else :#line:110
			O0OOO0000O0OO0O00 .time .delay (1 )#line:111
		for OOOO000O0OO00OOOO in O0OOO0000O0OO0O00 .event .get ():#line:113
			if OOOO000O0OO00OOOO .type ==O0OOO0000O0OO0O00 .QUIT :#line:114
				exit ()#line:115
class Entity :#line:118
	def __init__ (OOOO00OOOO0OO0O00 ,O0O00O00000O0000O ,O0OO0O000OOO0O0O0 ,O00OO00OO00OO0OOO ,OOOOO0OO000OOO00O ,OO0O0OOOOOO0000O0 ):#line:120
		OOOO00OOOO0OO0O00 .l11 =int (O0O00O00000O0000O )#line:121
		OOOO00OOOO0OO0O00 .l1l =int (O0OO0O000OOO0O0O0 )#line:122
		OOOO00OOOO0OO0O00 .ll1 =int (O00OO00OO00OO0OOO )#line:123
		OOOO00OOOO0OO0O00 .lll =font .render (O00OO00OO00OO0OOO ,1 ,(255 ,255 ,255 ))#line:124
		OOOO00OOOO0OO0O00 .delay =int (OOOOO0OO000OOO00O )#line:125
		OOOO00OOOO0OO0O00 .direction ="D"#line:126
		OOOO00OOOO0OO0O00 .target_edge =int (OO0O0OOOOOO0000O0 )#line:127
		OOOO00OOOO0OO0O00 .x =window_side //2 #line:128
		OOOO00OOOO0OO0O00 .y =0 #line:129
	def draw (OO00OO0OO00OOOO00 ):#line:131
		if OO00OO0OO00OOOO00 .l11 ==0 :#line:133
			O0OOO0000O0OO0O00 .draw .circle (window ,l11llll1ll [OO00OO0OO00OOOO00 .l1l ],(OO00OO0OO00OOOO00 .x ,OO00OO0OO00OOOO00 .y ),entity_half )#line:134
		elif OO00OO0OO00OOOO00 .l11 ==1 :#line:135
			O0OOO0000O0OO0O00 .draw .rect (window ,l11llll1ll [OO00OO0OO00OOOO00 .l1l ],(OO00OO0OO00OOOO00 .x -entity_half ,OO00OO0OO00OOOO00 .y -entity_half ,entity_side ,entity_side ))#line:136
		elif OO00OO0OO00OOOO00 .l11 ==2 :#line:137
			O0OOO0000O0OO0O00 .draw .polygon (window ,l11llll1ll [OO00OO0OO00OOOO00 .l1l ],((OO00OO0OO00OOOO00 .x ,OO00OO0OO00OOOO00 .y -entity_half ),(OO00OO0OO00OOOO00 .x +entity_half ,OO00OO0OO00OOOO00 .y ),(OO00OO0OO00OOOO00 .x ,OO00OO0OO00OOOO00 .y +entity_half ),(OO00OO0OO00OOOO00 .x -entity_half ,OO00OO0OO00OOOO00 .y )))#line:138
		elif OO00OO0OO00OOOO00 .l11 ==3 :#line:139
			O0OOO0000O0OO0O00 .draw .rect (window ,l11llll1ll [OO00OO0OO00OOOO00 .l1l ],(OO00OO0OO00OOOO00 .x -entity_half ,OO00OO0OO00OOOO00 .y -entity_half //2 ,entity_side ,entity_half ))#line:140
			O0OOO0000O0OO0O00 .draw .rect (window ,l11llll1ll [OO00OO0OO00OOOO00 .l1l ],(OO00OO0OO00OOOO00 .x -entity_half //2 ,OO00OO0OO00OOOO00 .y -entity_half ,entity_half ,entity_side ))#line:141
		elif OO00OO0OO00OOOO00 .l11 ==4 :#line:142
			O0OOO0000O0OO0O00 .draw .polygon (window ,l11llll1ll [OO00OO0OO00OOOO00 .l1l ],((OO00OO0OO00OOOO00 .x ,OO00OO0OO00OOOO00 .y -entity_half ),(OO00OO0OO00OOOO00 .x +entity_half ,OO00OO0OO00OOOO00 .y +entity_half ),(OO00OO0OO00OOOO00 .x -entity_half ,OO00OO0OO00OOOO00 .y +entity_half )))#line:143
		else :#line:144
			O0OOO0000O0OO0O00 .draw .polygon (window ,l11llll1ll [OO00OO0OO00OOOO00 .l1l ],((OO00OO0OO00OOOO00 .x +0 ,OO00OO0OO00OOOO00 .y +-15 ),(OO00OO0OO00OOOO00 .x +-14 ,OO00OO0OO00OOOO00 .y +-5 ),(OO00OO0OO00OOOO00 .x +-9 ,OO00OO0OO00OOOO00 .y +12 ),(OO00OO0OO00OOOO00 .x +9 ,OO00OO0OO00OOOO00 .y +12 ),(OO00OO0OO00OOOO00 .x +14 ,OO00OO0OO00OOOO00 .y +-5 )))#line:145
		window .blit (OO00OO0OO00OOOO00 .lll ,(OO00OO0OO00OOOO00 .x -font_half_wide ,OO00OO0OO00OOOO00 .y -font_half_high ))#line:148
		if OO00OO0OO00OOOO00 .target_edge ==0 :#line:150
			O0OOO0000O0OO0O00 .draw .line (window ,(255 ,255 ,0 ),(OO00OO0OO00OOOO00 .x -10 ,OO00OO0OO00OOOO00 .y +25 ),(OO00OO0OO00OOOO00 .x +10 ,OO00OO0OO00OOOO00 .y +25 ),3 )#line:151
			O0OOO0000O0OO0O00 .draw .line (window ,(255 ,255 ,0 ),(OO00OO0OO00OOOO00 .x -10 ,OO00OO0OO00OOOO00 .y +25 ),(OO00OO0OO00OOOO00 .x -5 ,OO00OO0OO00OOOO00 .y +20 ),3 )#line:152
			O0OOO0000O0OO0O00 .draw .line (window ,(255 ,255 ,0 ),(OO00OO0OO00OOOO00 .x -10 ,OO00OO0OO00OOOO00 .y +25 ),(OO00OO0OO00OOOO00 .x -5 ,OO00OO0OO00OOOO00 .y +30 ),3 )#line:153
		elif OO00OO0OO00OOOO00 .target_edge ==1 :#line:154
			O0OOO0000O0OO0O00 .draw .line (window ,(255 ,255 ,0 ),(OO00OO0OO00OOOO00 .x -10 ,OO00OO0OO00OOOO00 .y +25 ),(OO00OO0OO00OOOO00 .x +10 ,OO00OO0OO00OOOO00 .y +25 ),3 )#line:155
			O0OOO0000O0OO0O00 .draw .line (window ,(255 ,255 ,0 ),(OO00OO0OO00OOOO00 .x +10 ,OO00OO0OO00OOOO00 .y +25 ),(OO00OO0OO00OOOO00 .x +5 ,OO00OO0OO00OOOO00 .y +20 ),3 )#line:156
			O0OOO0000O0OO0O00 .draw .line (window ,(255 ,255 ,0 ),(OO00OO0OO00OOOO00 .x +10 ,OO00OO0OO00OOOO00 .y +25 ),(OO00OO0OO00OOOO00 .x +5 ,OO00OO0OO00OOOO00 .y +30 ),3 )#line:157
		elif OO00OO0OO00OOOO00 .target_edge ==2 :#line:158
			O0OOO0000O0OO0O00 .draw .line (window ,(255 ,255 ,0 ),(OO00OO0OO00OOOO00 .x ,OO00OO0OO00OOOO00 .y +20 ),(OO00OO0OO00OOOO00 .x ,OO00OO0OO00OOOO00 .y +40 ),3 )#line:159
			O0OOO0000O0OO0O00 .draw .line (window ,(255 ,255 ,0 ),(OO00OO0OO00OOOO00 .x ,OO00OO0OO00OOOO00 .y +40 ),(OO00OO0OO00OOOO00 .x -5 ,OO00OO0OO00OOOO00 .y +35 ),3 )#line:160
			O0OOO0000O0OO0O00 .draw .line (window ,(255 ,255 ,0 ),(OO00OO0OO00OOOO00 .x ,OO00OO0OO00OOOO00 .y +40 ),(OO00OO0OO00OOOO00 .x +5 ,OO00OO0OO00OOOO00 .y +35 ),3 )#line:161
		
def __O0O0OOOOOOOOO0OO0(e):
	return e.l11 == 0

def __OO0OO0O00O000OOO0(e):
	return e.l11 == 1

def __OO00OOOOO00OO0OOO(e):
	return e.l11 == 2

def __O0OOO00OOOO00O000(e):
	return e.l11 == 3

def __OOOO000OOO00OO000(e):
	return e.l11 == 4

def __O00OOOO0OO0OOO00O(e):
	return e.l11 == 5

def __O000OOO0000OO000O(e):
	return e.l1l == 0

def __OO000OO0OO000OOOO(e):
	return e.l1l == 1

def __O0O0O0000000OOO00(e):
	return e.l1l == 2

def __OO00OOO0O0O00000O(e):
	return e.l1l == 3
	
def __O00O00O000O0O0OO0(e):
	return e.l1l == 4
		
def __O0OOO0O0OOO0O0OOO(e):
	return e.l1l == 5
		
def __O0OO000OOOOOO000O(e, d):
	return e.ll1 % d == 0
	
def is_inside_a_circle(e):
	return __O0O0OOOOOOOOO0OO0(e)

def wrapped_in_a_circle(e):
	return __O0O0OOOOOOOOO0OO0(e)
	
def is_shaped_like_a_circle(e):
	return __O0O0OOOOOOOOO0OO0(e)

def is_inside_a_square(e):
	return __OO0OO0O00O000OOO0(e)

def wrapped_in_a_square(e):
	return __OO0OO0O00O000OOO0(e)
	
def is_shaped_like_a_square(e):
	return __OO0OO0O00O000OOO0(e)

def is_inside_a_diamond(e):
	return __OO00OOOOO00OO0OOO(e)

def wrapped_in_a_diamond(e):
	return __OO00OOOOO00OO0OOO(e)
	
def is_shaped_like_a_diamond(e):
	return __OO00OOOOO00OO0OOO(e)

def is_inside_a_cross(e):
	return __O0OOO00OOOO00O000(e)

def wrapped_in_a_cross(e):
	return __O0OOO00OOOO00O000(e)
	
def is_shaped_like_a_cross(e):
	return __O0OOO00OOOO00O000(e)

def is_inside_a_triangle(e):
	return __OOOO000OOO00OO000(e)

def wrapped_in_a_triangle(e):
	return __OOOO000OOO00OO000(e)
	
def is_shaped_like_a_triangle(e):
	return __OOOO000OOO00OO000(e)

def is_inside_a_pentagon(e):
	return __O00OOOO0OO0OOO00O(e)

def wrapped_in_a_pentagon(e):
	return __O00OOOO0OO0OOO00O(e)
	
def is_shaped_like_a_pentagon(e):
	return __O00OOOO0OO0OOO00O(e)
	
def is_colored_red(e):
	return __O000OOO0000OO000O(e)

def color_is_red(e):
	return __O000OOO0000OO000O(e)

def painted_red(e):
	return __O000OOO0000OO000O(e)

def is_colored_orange(e):
	return __OO000OO0OO000OOOO(e)

def color_is_orange(e):
	return __OO000OO0OO000OOOO(e)

def painted_orange(e):
	return __OO000OO0OO000OOOO(e)

def is_colored_green(e):
	return __O0O0O0000000OOO00(e)

def color_is_green(e):
	return __O0O0O0000000OOO00(e)

def painted_green(e):
	return __O0O0O0000000OOO00(e)

def is_colored_blue(e):
	return __OO00OOO0O0O00000O(e)

def color_is_blue(e):
	return __OO00OOO0O0O00000O(e)

def painted_blue(e):
	return __OO00OOO0O0O00000O(e)

def is_colored_purple(e):
	return __O00O00O000O0O0OO0(e)

def color_is_purple(e):
	return __O00O00O000O0O0OO0(e)

def painted_purple(e):
	return __O00O00O000O0O0OO0(e)	

def is_colored_black(e):
	return __O0OOO0O0OOO0O0OOO(e)

def color_is_black(e):
	return __O0OOO0O0OOO0O0OOO(e)

def painted_black(e):
	return __O0OOO0O0OOO0O0OOO(e)	
	
def is_divisible_by(e, d):
	return __O0OO000OOOOOO000O(e, d)	
	
def evenly_divides_by(e, d):
	return __O0OO000OOOOOO000O(e, d)

def divides_evenly_by(e, d):
	return __O0OO000OOOOOO000O(e, d)