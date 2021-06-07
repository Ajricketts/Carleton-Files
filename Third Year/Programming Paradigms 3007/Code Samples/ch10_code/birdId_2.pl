%source and credit to: 
%http://www.amzi.com/ExpertSystemsInProlog/index.htm
%modified by A.Runka

bird(laysan_albatross):-
	fact(family(albatross)),
	fact(color(white)).

bird(black_footed_albatross):-
	fact(family(albatross)),
	fact(color(dark)).

bird(whistling_swan) :-
	fact(family(swan)),
	fact(voice(muffled_musical_whistle)).

bird(trumpeter_swan) :-
	fact(family(swan)),
	fact(voice(loud_trumpeting)).

fact(X):-
	X =.. [F|Args],   %f(a,b,c) -> [f, a, b, c]
	fact(F,Args).
fact(X,Y):-
	ask(X,Y).
	
%ask about data
ask(Attr,Val):-
	write(Attr: Val),
	write('?'),
	read(yes).   %only unifies with user input 'yes'

