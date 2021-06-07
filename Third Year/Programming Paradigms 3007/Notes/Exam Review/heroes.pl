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
   What super powers does spiderman have?
?- hero(spiderman, powers(Powers))

    Who's super power is 'intelligence'?
?- hero(Name, powers(Power)), member(intelligence, Power).

    Do any two heroes have the same super power?
?- hero(Name1, powers(Power1)), hero(Name2, powers(Power2)), Name1\=Name2, member(CommonPower, Power1), member(CommonPower, Power2).

    Who is a member of the avengers?
?- affiliation(Name, avengers).

    What member(s) of the xmen has the power of flight?
?- affiliation(Name, xmen), hero(Name, powers(Power)), member(flight, Power).

    Do any members of different groups share the same power?
?- affiliation(Name1, Group1), affiliation(Name2, Group2), hero(Name1, powers(Power1)), hero(Name2, powers(Power2)), Name1\=Name2, member(CommonPower, Power1), member(CommonPower, Power2).

    Which superhero has the most powers?
?- hero(Hero,powers(Powers)),length(Powers,Len), not((hero(_,powers(P)),length(P,L),L>Len)).
*/
