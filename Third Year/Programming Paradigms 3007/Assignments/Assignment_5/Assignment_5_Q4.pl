%COMP 3007 Programming Paradigms
%Alyxander-Jacob Ricketts
%101084146


%Check for the empty list (also base case)
list([]).

%See if there is at least one item in the list (check the tail of the list)
list([_|L]):- list(L).


%Test cases
%-------------
%?- list([1, 2, 3]).
%Output: true.

%?- list(hello).
%Output: false.

%?- list([]).
%Output: true.
