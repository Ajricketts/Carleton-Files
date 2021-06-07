contains(X, [X|_]).
contains(X, [_|T]):- contains(X,T).

%len(List,Length) True if there are Length items in the List.

len([],0).
len([_|T],Result):-
	len(T,LenT),
	Result is LenT+1.

%len([1,2,3],X)
%X = Result, Result is LenT+1, LenT = Result', Result' = LenT'+1, ... =0
%'
%lenit([],0).
%lenit([_|T],Result):-
%	Result is LenT+1,
%	lenit(T,LenT).


lenit(L,R):-
	lenit(L,0,R).

lenit([],R,R).
lenit([_|T],A,R):-
	A1 is A+1,
	lenit(T,A1,R).


join([], L, L).
join([H|L1], L2, [H|L3]):-
    join(L1, L2, L3).

%join([1,2,3],[a,b,c],R)

%R = [1|L3], L3= [2|L3'], L3' = [3|L3''], L3'' = [a,b,c]
%[1|[2|[3|[a,b,c]]]] => [1,2,3,a,b,c]

del_first(X, [X|T], T).
del_first(X, [H | T], [H | Result]):-
     X \= H,
     del_first(X,T,Result).


del(X, [X|T], T).
del(X, [H|T], [H|Result]):- del(X,T,Result).

del_all(_, [], []).
del_all(X, [X|T], Result):- del_all(X,T,Result).
del_all(X, [H|T], [H|Result]):- X\=H, del_all(X,T,Result).

%homework
%del_nth(X, N, L, R). true if R is the result of L removed with the nth copy of X removed.



selects([], [L]):- is_list(L).
selects([X|Xs], Ys):-
      del(X, Ys, Ys1),
      selects(Xs,Ys1).


mySort([],[]).
mySort([H|T],Result):-
	mySort(T,SortedTail),
	insert(H,SortedTail,Result).

insert(Item,[],[Item]).
insert(Item,[H|T],[Item,H|T]):-
	Item=<H.
insert(Item,[H|T],[H|R]):-
	Item>H,
	insert(Item,T,R).

%iterative max
max([H|T],R):-
	max(T,H,R).

max([],R,R).
max([H|T],LSF,R):-
	H>LSF,
	max(T,H,R).
max([H|T],LSF,R):-
	H=<LSF,
	max(T,LSF,R).

%(homework): write this recursively


%even_list(L) - true if there are an even number of elements in the list.

even_list([]).
%even_list([X,Y]).
even_list([_,_|T]):-even_list(T).

%even_items(L) - true if all items in the list are even numbers
even_items([]).
even_items([H|T]):-
	Res is H mod 2,
	Res == 0,
	even_items(T).


sum_list([],0).
sum_list([H|T],R):-
	sum_list(T,TailSum),
	R is TailSum+H.

sum_it(L,R):-
	sum_it(L,0,R).

sum_it([],A,A).
sum_it([H|T],A,R):-
	A1 is A+H,
	sum_it(T,A1,R).

%scale(Factor,L,R) - true if R is the items in L scaled by Factor.

scale(1,L,L).
scale(_,[],[]).
scale(F,[H|T],[MappedValue|R]):-
	MappedValue is F*H,
	scale(F,T,R).

square(X,X2):- X2 is X*X.
map(_,[],[]).
map(Func,[H|T],[X|R]):-
	call(Func,H,X),
	map(Func,T,R).


treescale(_,[],[]).
treescale(F,[H|T],[RH|RT]):-
	is_list(H),
	treescale(F,H,RH),
	treescale(F,T,RT).
treescale(F,[H|T],[RH|RT]):-
	number(H),
	RH is H * F,
	treescale(F,T,RT).
