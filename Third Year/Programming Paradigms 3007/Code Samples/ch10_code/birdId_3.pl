%source and credit to: 
%http://www.amzi.com/ExpertSystemsInProlog/index.htm
%modified by A.Runka

:- dynamic known/3.  %let swi know we'll be building this through asserts

bird(laysan_albatross):-
	fact(family(albatross)),
	fact(color(white)).

bird(black_footed_albatross):-
	fact(family(albatross)),
	fact(color(dark)).
	
bird(imaginary_green_albatross):-
	fact(family(albatross)),
	fact(color(green)).

bird(whistling_swan) :-
	fact(family(swan)),
	fact(voice(muffled_musical_whistle)).

bird(trumpeter_swan) :-
	fact(family(swan)),
	fact(voice(loud_trumpeting)).


fact(X):-
	X =.. [F|Args],   %family(albatross) -> [family, albatross]
	fact(F,Args).

%check known values
fact(X,Y):-
	known(yes,X,Y),!. %we know its yes
fact(X,Y):-
	known(_,X,Y),!,fail. %we know its not yes
%unknown so ask
fact(X,Y):-
	ask(X,Y).

	
ask(A, V):-
	write(A:V), % ask user
	write('? : '),
	read(Response), % get the answer
	assert(known(Response, A, V)), % remember it
	Response == yes. % succeed or fail

%clear all known facts
restart:-retractall(known(_,_,_)).