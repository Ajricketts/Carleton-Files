%hero(Name,Powers)
hero(spiderman,powers([webslinging, strength, heightened_reflexes])).
hero(thor,powers([strength, hammer])).
hero(ironman,powers([money,intelligence,power_armor])).
hero(hulk, powers([transformation, strength])).
hero(wolverine, powers([healing, claws, heightened_senses])).
hero(superman, powers([strength, flight, heightened_senses,invulnerability, eye_lazers, xray_vision])).
hero(rogue, powers([strength, flight, power_steal])).
hero(storm, powers([weather_control, flight])).
hero(batman, powers([money, heightened_reflexes, intelligence])).
hero(antman, powers([power_armor, resizeable])).
hero(cyclops, powers([eye_lazers])).
hero(wonder_woman, powers([strength, flight, heightened_senses, heightened_reflexes])).
hero(dr_strange, powers([magic, intelligence])).
hero(aquaman, powers([fish])).
hero(captain_america, powers([strength, speed, heightened_reflexes])).
hero(punisher, powers([guns,rage])).
hero(prof_x, powers([telepathy, telekinesis])).

	
%affiliation(Name,Group)
affiliation(thor,avengers).
affiliation(ironman,avengers).
affiliation(hulk,avengers).
affiliation(wolverine, xmen).
affiliation(superman, justice_league).
affiliation(rogue, xmen).
affiliation(storm, xmen).
affiliation(batman, justice_league).
affiliation(cyclops, xmen).
affiliation(wonder_woman, justice_league).
affiliation(aquaman, justice_league).
affiliation(captain_america, avengers).
affiliation(prof_x, xmen).


/*
%    What super powers does spiderman have?
%?- hero(spiderman, powers(Powers)).

%    Who's super power is 'intelligence'?
%?- hero(Hero, powers(Powers)), member(intelligence,Powers).

%    Do any two heroes have the same super power?
%?- hero(Hero1, powers(Powers1)), hero(Hero2, powers(Powers2)), Hero1\=Hero2, member(CommonPower,Powers1), member(CommonPower,Powers2).

%    Who is a member of the avengers?
%?- affiliation(Hero,avengers).

%    What member(s) of the xmen has the power of flight?
%?- affiliation(Hero,xmen),hero(Hero,powers(Powers)),member(flight,Powers).

%    Do any members of different groups share the same power?
%?- affiliation(Hero1,Group1), affiliation(Hero2,Group2), Hero1\=Hero2, Group1\=Group2, hero(Hero1,powers(Powers1)),hero(Hero2,powers(Powers2)), member(CommonPower,Powers1), member(CommonPower,Powers2).

%    Which superhero has the most powers?
%?- hero(Hero,powers(Powers)),length(Powers,Len), not((hero(_,powers(P)),length(P,L),L>Len)).
*/