%COMP 3007 Programming Paradigms
%Alyxander-Jacob Ricketts
%101084146

%male(Name).  %Male Facts
male(aj).
male(john).
male(miro).
male(peter).
male(peterjr).

%Test cases
%-------------
%male(peter).
%Output: true

%male(aj).
%Output: true

%male(august).
%Output: false


%female(Name).  %female facts
female(karen).
female(august).
female(delores).
female(diana).

%Test cases
%-------------
%female(delores).
%Output: true

%female(aj).
%output(false).

%female(diana).
%Output: true



%parent(X,Y).   %Parent Facts
parent(karen, aj).
parent(karen,miro).
parent(karen,august).
parent(delores,karen).
parent(peter,karen).
parent(peter,peterjr).
parent(delores,peterjr).

%Test cases
%-------------
%parent(karen,august).
%Output: true

%parent(delores,karen).
%Output: True

%parent(aj,karen).
%false: false




%is_mother(X).  %Mother Facts
is_mother(X):- female(X), parent(X,_).

%Test cases
%-------------
%is_mother(karen)
%Output: true

%is_mother(aj)
%Output: false

%Father Facts
%is_father(X).
is_father(X):- male(X), parent(X,_).

%Test cases
%-------------

%is_father(aj)
%Output: false

%is_father(karen)
%Output: false

%is_father(peter)
%Output: true




%Uncle Facts
%is_uncle(X,Y).
is_uncle(peterjr,aj).
is_uncle(peterjr,august).
is_uncle(peterjr,miro).

%Test cases
%-------------
%is_uncle(aj,august)
%Output: false

%is_uncle(peterjr,aj)
%Output: true



%Aunt Facts
%is_aunt(X,Y).
is_aunt(diana,aj).
is_aunt(diana,august).
is_aunt(diana,miro).

%Test cases
%-------------
%is_aunt(diana,aj).
%Output:True

%is_aunt(aj,diana).
%Output:true



%Sister Facts
%sister(X,Y).
sister(august,aj).
sister(august,miro).

%Test cases
%-------------
%sister(august,miro).
%Output: true

%sister(aj,miro).
%Output: false


%Brother Facts
%brother(X,Y).
brother(aj,miro).
brother(aj,august).
brother(miro,august).
brother(miro,aj).

%Test cases
%-------------
%brother(aj,august).
%Output: true

%brother(miro,august).
%Output: true

%brother(august,aj).
%Output: false




%Grandfather Facts
%grandfather(X,Y).
grandfather(peter,aj).
grandfather(peter,august).
grandfather(peter,miro).

%Test cases
%-------------
%grandfather(peter,august).
%Output: true

%grandfather(aj,peter).
%Output: false

%Grandmother Facts
%grandmother(X,Y).
grandmother(delores,aj).
grandmother(delores,august).
grandmother(delores,miro).

%Test cases
%-------------
%grandmother(delores,august).
%Output: true

%grandmother(delores,miro).
%Output: true

%grandmother(delores,peter).
%Output: false


%Ancestor Facts
%ancestor(X,Y).
ancestor(peter,aj).
ancestor(peter,august).
ancestor(peter,karen).
ancestor(peter,peterjr).
ancestor(peter,miro).
ancestor(delores,aj).
ancestor(delores,august).
ancestor(delores,karen).
ancestor(delores,peterjr).
ancestor(delores,miro).
ancestor(karen,aj).
ancestor(karen,miro).
ancestor(karen,miro).
ancestor(peterjr,aj).
ancestor(peterjr,miro).
ancestor(peterjr,miro).

%Test cases
%-------------
%ancestor(delores,karen).
%Output: true

%ancestor(delores,peterjr).
%Output: true

%ancestor(aj,karen).
%Output: false
