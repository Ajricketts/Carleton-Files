%Cody Bennett - 101035873
%A)
lastEle(Atom,[Atom]).%reached final element
lastEle(Atom,[_|T]):-lastEle(Atom,T).%still elements in list-split into head/tail

%Testcases:
%?- lastEle(X,[how,are,you,today]).
%Result:
%X = today .
%?- lastEle(X,[1,2,3,4]).
%Result:
%X = 4

%B)
letter(X, Z):-X>80,X<100->Z='a'.
letter(X, Z):-X>70,X<80->Z='b'.
letter(X, Z):-X>60,X<70->Z='c'.
letter(X, Z):-X>50,X<60->Z='d'.
letter(X,Z):-X<50->Z='f'.
%above functions translate number to corr letter

gradeMap([],[]).
gradeMap([L|T],[X|Y]):-
    letter(L,Z),
    X=Z,
    gradeMap(T,Y).%change first value from number to letter then incr to next


%Testcases:
%?-gradeMap([0, 16, 49, 55, 63, 78, 92], R).
%R=[f,f,f,d,c,b,a]

%C)
split([],_,[],[]).
split([H|T],Pivot,L1,[H|Y]):-
    H>=Pivot,
    split(T,Pivot,L1,Y).%sort to bigger list
split([H|T],Pivot,[H|Y],L2):-
    H<Pivot,
    split(T,Pivot,Y,L2).%sort to smaller list
%Testcases:
%?- split([4,7,1,8,2,9,3],5, L1, L2).
%Result:
%L1 = [4, 1, 2, 3],
%L2 = [7, 8, 9] .
%?- split([4,7,1,8,2,9,3],5, [4,1,2,3], [7, 8, 9]).
%Result:
%true

%D)
start(X,[H|_]):-X=H.
myNextto(X,Y,[H|T]):-H=X,start(Y,T).%checks if first value =x then send tail(next val) to see if H of T is Y(IE. beside each other)
myNextto(X,Y,[_|T]):-myNextto(X,Y,T).%goes to next val if H isn't X(send T to myNextto)

%Testcases:
%?- myNextto(a,b, [c,a,b,d]).
%Result:
%true
%?- myNextto(a,b, [c,a,d,b]).
%Result:
%false
