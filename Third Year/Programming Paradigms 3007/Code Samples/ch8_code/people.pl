person(alice, 20).
person(bob, 21).
person(charlie, 23).
person(dave, 20).

hobby(alice, birdwatching).
hobby(alice, programming).
hobby(bob, larping).
hobby(charlie, larping).
hobby(charlie, birdwatching).
hobby(dave, birdwatching).

friends(Person1, Person2):-
		hobby(Person1,Hobby),
		hobby(Person2,Hobby),
		Person1 \= Person2,
		person(Person1,Age1),
		person(Person2,Age2),
		AgeDiff is abs(Age2-Age1),
		AgeDiff =< 2 .

%?-friends(alice,dave).
%hobby(alice,Hobby),hobby(dave,Hobby),alice\=dave,person(alice,Age1),person(dave,Age2),AgeDiff is abs(Age2-Age1), AgeDiff =< 2 .
%hobby(dave,birdwatching),alice\=dave,person(alice,Age1),person(dave,Age2),AgeDiff is abs(Age2-Age1), AgeDiff =< 2 .
%alice\=dave,person(alice,Age1),person(dave,Age2),AgeDiff is abs(Age2-Age1), AgeDiff =< 2 .
%person(alice,Age1),person(dave,Age2),AgeDiff is abs(Age2-Age1), AgeDiff =< 2 .
%person(dave,Age2),AgeDiff is abs(Age2-20), AgeDiff =< 2 .
%AgeDiff is abs(20-20), AgeDiff =< 2 .
%0 =< 2 .
%true.	