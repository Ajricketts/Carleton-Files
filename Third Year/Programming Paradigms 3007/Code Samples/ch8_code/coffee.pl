%manager(Name).
manager(mary).
manager(john).
manager(bob).

%bill(Manager,ID,Amount).

bill(john,1,14).
bill(mary,2,25).
bill(mary,3,12).
bill(bob,4,5).
bill(john,5,7).
bill(john,6,5).
bill(john,7,15).
bill(john,8,2).
bill(john,9,16).

%paid(ID,Amount).
paid(1,15).
paid(2,20).
paid(3,12).
paid(5,17).

%is bob a manager?
%?- manager(bob).

%who is a manager?
%?- manager(Person).

%what bills have been paid?
%?- paid(Id,_).

%how much was bill #2 worth?
%?- bill(_,2,Amt).

%did mary pay bill 3?
%?-  bill(mary,3,_),paid(3,_).

% which managers have been sent a bill for less than 10 dollars?
%?- manager(Name),bill(Name,Id,Amt),Amt<10.


% who has been sent more than one bill?
%?- bill(Name,Id,_),bill(Name,Id2,_),Id\=Id2.

% who has made a payment less than the amount of their bill?
%?- bill(Manager,Id,Cost),paid(Id,Paid), Cost>Paid.

% Who has received a bill but not paid it?
%?- bill(Name,Id,_),not(paid(Id,_)).

% What is the largest bill given to john?
%?- bill(john,Id,Amt), not((bill(john,Id2,Amt2),Amt2>Amt)).

% Who was given the smallest bill?
%?-  bill(Name,Id,Amt), not((bill(_,_,Amt2),Amt2<Amt)).


smallestBill(Name):-
 bill(Name,Id,Amt), not((bill(_,_,Amt2),Amt2<Amt)).