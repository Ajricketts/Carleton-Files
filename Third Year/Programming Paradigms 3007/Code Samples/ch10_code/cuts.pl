contains(X,[X|_]):- !.
contains(X,[_|T]):- contains(X,T).

fact(a).
fact(b).

has(bob,phone).
has(alice,keys).
has(alice,wallet).
has(bob,emergency).

ready(X):-prepared(X).
ready(X):-has(X,emergency).

prepared(X):- has(X,phone),!,has(X,keys),has(X,wallet).
prepared(X):- has(_,phone),has(_,keys),has(_,wallet).  %always true, but never seen


sum_one_to(1,1):-!.
sum_one_to(N, Result):-
    N1 is N - 1,
    sum_one_to(N1,Result1),
    Result is Result1 + N.
	
naht(P):-P,!,fail.
naht(P).


f2(X,-1):-X<0.
f2(X,1).