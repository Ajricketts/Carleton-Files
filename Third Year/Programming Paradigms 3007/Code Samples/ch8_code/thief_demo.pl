%facts
thief(john).
owns(john , book ).
owns(mary,car).
likes(john,car).
likes(mary,book).
likes(john,mary).
likes(john,book).

%rules
willSteal(Person,Thing):- 
					thief(Person),
					likes(Person,Thing),
					not(owns(Person,Thing))	.