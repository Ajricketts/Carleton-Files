witch(X):- female(X), hasWart(X), turnedIntoNewt(X,Y).
warlock(X):- male(X), hasWart(X), turnedIntoNewt(X,Y).

turnedIntoNewt(X,Y):- wasNewt(Y), not(gotBetter(Y)).

female(glenda).
hasWart(glenda).

male(steve).
wasNewt(steve).
gotBetter(steve).

witch(X):- burns(X), female(X).
warlock(X):- burns(X), male(X).

burns(X):-wooden(X).
wooden(X):-floats(X).

floats(rain).
floats(apples).
floats(smallrocks).
floats(gravy).
floats(aDuck). %!
floats(X):- sameWeight(X,Y),floats(Y).

sameWeight(glenda,aDuck).

male(aDuck).
