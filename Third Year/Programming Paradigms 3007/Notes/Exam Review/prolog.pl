f(N,N):- N<4.
f(N,R):-
	N>3,
	N1 is N-1,
	N2 is N-2,
	N3 is N-3,
	f(N1,R1),
	f(N2,R2),
	f(N3,R3),
	R is R1 + (2*R2)+ (3*R3).
	

fit(N,N):-N<4.	
fit(N,R):-
	N>3,
	iter(N,3, 2, 1,R).
	
iter(3,R,_,_,R).
iter(C,N1,N2,N3,R):-
	C1 is C-1,
	N is N1 + (2*N2)+ (3*N3),	
	iter(C1,N,N1,N2,R).
	
	
squareList([],[]).
squareList([H|T],[H1|R]):-
	H1 is H*H,
	squareList(T,R).
	
multList([],1).
multList([H|T],R):-
	multList(T,R1),
	R is R1*H.


meanList(L,Mean):-
	sumList(L,R),
	countNums(L,N),
	Mean is R/N.
	
sumList([],0).
sumList([H|T],Sum):-
	number(H),
	sumList(T,R),
	Sum is H+R.
sumList([H|T],Sum):-
	atom(H),
	sumList(T,Sum).

countNums([],0).
countNums([H|T],Count):-
		number(H),
		countNums(T,R),
		Count is R+1.
countNums([H|T],Count):-
		atom(H),
		countNums(T,Count).

