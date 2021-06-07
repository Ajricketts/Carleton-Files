%COMP 3007 Programming Paradigms
%Alyxander-Jacob Ricketts
%101084146

lastele(X,[X]).
lastele(X,[_|Y]):- lastele(X,Y).

%Test cases
%-------------
%?- lastEle(X,[how,are,you,today]).

%Output:
%X = today


%These predicates switch the grade numbers for letters
grades(X,Z):- X >= 80,X < 100->Z='A'.
grades(X,Z):- X >= 70,X < 80->Z='B'.
grades(X,Z):- X >= 60,X < 70->Z='C'.
grades(X,Z):- X >= 50,X < 60->Z='D'.
grades(X,Z):- X < 50->Z='F'.


gradeMap([],[]). %Base case
gradeMap([H|T], [X|Y]) :-
    grades(H,Z),      %Get the letter grade
    X=Z,              %Add the letter grade to the 'new' list
    gradeMap(T,Y).    %Continue on with the tail of the first and second lists

%Test cases
%-------------
%gradeMap([0, 34, 47, 52, 68, 75, 98], X).
%Output:
        %X = ['F', 'F', 'F', 'D', 'C', 'B', 'A']

%gradeMap([1, 50, 80, 65], X).
%Output:
        %X = ['F', 'D', 'A', 'C'].



split([],_,[],[]).
split([H|T],Pivot,L1,[H|Y]):-
    %If the head of the list is greater than the pivot
     %add it to the second list
    H>=Pivot->split(T,Pivot,L1,Y).

split([H|T],Pivot,[H|Y],L2):-
    %If the head of the list is greater than the pivot
     %add it to the first list
    H<Pivot->split(T,Pivot,Y,L2).

%Test cases
%-------------
%?- split([9,5,6,1,4,2,5,8,10],5, L1, L2).
%Output:
    %L1 = [1, 4, 2],
    %L2 = [9, 5, 6, 5, 8, 10]

%?- split([9,5,6,1,4,2,5,8,10],5, [1,4,2], [9,5,6,5,8,10]).
%Output: true


beside(X,[H|_]):-X=H.

%First check to see if the head of the list is X, if it is not this fails and then
 %this will go to the next predicate, if the head is X then check to see if the
 %head of the tail is Y (The value you want to determine if it is beside X or not)
myNextto(X,Y,[H|T]):-H=X,beside(Y,T).

%skip to next value in the list if the head of the list isn't the desired value (X)'
myNextto(X,Y,[_|T]):-myNextto(X,Y,T).


%Test cases
%-------------
%?- myNextto(a,b, [c,a,b,d]).
%Output: true
%?- myNextto(a,b, [c,a,d,b]).
%Output: false
%?-myNextto(b,c,[a,b,d,f,b,c]).
%Output: true
