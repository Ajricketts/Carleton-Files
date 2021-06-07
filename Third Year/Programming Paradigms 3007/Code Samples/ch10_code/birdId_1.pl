%source and credit to: 
%http://www.amzi.com/ExpertSystemsInProlog/index.htm
%modified by A.Runka

bird(laysan_albatross):-
	family(albatross),
	color(white).

bird(black_footed_albatross):-
	family(albatross),
	color(dark).

bird(whistling_swan) :-
	family(swan),
	voice(muffled_musical_whistle).

bird(trumpeter_swan) :-
	family(swan),
	voice(loud_trumpeting).

