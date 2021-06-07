%player(name(First,Last),team(City),pos(Position),stats(Goals,Assists,Shots))
player(name(alex,ovechkin),team(was),pos(lw),stats(51,38,338)).
player(name(marcus,pettersson),team(pit),pos(d),stats(2,23,87)).
player(name(kevin,fiala),team(min),pos(lw),stats(13,26,174)).
player(name(ryan,hartman),team(min),pos(rw),stats(12,14,145)).
player(name(leon,driasaitl),team(edm),pos(c),stats(50,55,231)).
player(name(john,tavares),team(tor),pos(c),stats(47,41,286)).
player(name(steven,stamkos),team(tb),pos(c),stats(45,53,234)).
player(name(nikita,kucherov),team(tb),pos(rw),stats(41,87,246)).
player(name(nathan,mackinnon),team(col),pos(c),stats(41,58,365)).
player(name(alex,debrincat),team(chi),pos(rw),stats(41,35,220)).
player(name(jake,guentzel),team(pit),pos(lw),stats(40,36,227)).
player(name(jeff,skinner),team(buf),pos(lw),stats(40,23,268)).
player(name(mark,scheifele),team(wpg),pos(c),stats(38,46,199)).
player(name(johnny,gaudreau),team(cgy),pos(lw),stats(36,63,245)).
player(name(mike,hoffman),team(fla),pos(lw),stats(36,34,253)).
player(name(aleksander,barkov),team(fla),pos(c),stats(35,61,206)).
player(name(morgan,rielly),team(tor),pos(d),stats(20,52,223)).
player(name(brent,burns),team(sj),pos(d),stats(16,67,300)).
player(name(patrick,kane),team(chi),pos(rw),stats(44,66,341)).


%On what team does Leon Driasaitl play, and in what position?
%?-player(name(leon,driasaitl),team(City),pos(Position),_).

%What is the last name of any player who has at most 15 goals?
%?-player(name(_,Last),_,_,stats(Goals,_,_)),Goals =< 15.

    %Output:
    %Last = pettersson,
    %Goals = 2 ;
    %Last = fiala,
    %Goals = 13 ;
    %Last = hartman,
    %Goals = 12 ;
    %false.

%Who plays defence? (find one name at a time via backtracking)
%?-player(name(First,Last),_,pos(d),_).

    %Output:
    %First = marcus,
    %Last = pettersson ;
    %First = morgan,
    %Last = rielly ;
    %First = brent,
    %Last = burns ;
    %false.

%What teams have a player with the first name "Alex"?
%?player(name(alex,_),team(City),_,_).
%or
%?player(name(alex,_),team(Team),_,_). if you want the output to say team instead of City

    %Output:
    %Team = was ;
    %Team = chi.

%What pairs of players play on the same team? (list one pair at a time using backtracking)
%%player(name(First1,Last1),team(City),_,_),player(name(First2,Last2),team(City),_,_),Last1\=Last2.

    %Output:
    %First1 = marcus,
    %Last1 = pettersson,
    %City = pit,
    %First2 = jake,
    %Last2 = guentzel ;
    %First1 = kevin,
    %Last1 = fiala,
    %City = min,
    %First2 = ryan,
    %Last2 = hartman ;
    %First1 = ryan,
    %Last1 = hartman,
    %City = min,
    %First2 = kevin,
    %Last2 = fiala ;
    %First1 = john,
    %Last1 = tavares,
    %City = tor,
    %First2 = morgan,
    %Last2 = rielly ;
    %First1 = steven,
    %Last1 = stamkos,
    %City = tb,
    %First2 = nikita,
    %Last2 = kucherov ;
    %First1 = nikita,
    %Last1 = kucherov,
    %City = tb,
    %First2 = steven,
    %Last2 = stamkos ;
    %First1 = alex,
    %Last1 = debrincat,
    %City = chi,
    %First2 = patrick,
    %Last2 = kane ;
    %First1 = jake,
    %Last1 = guentzel,
    %City = pit,
    %irst2 = marcus,
    %ast2 = pettersson ;
    %First1 = mike,
    %Last1 = hoffman,
    %City = fla,
    %First2 = aleksander,
    %Last2 = barkov ;
    %First1 = aleksander,
    %Last1 = barkov,
    %City = fla,
    %First2 = mike,
    %Last2 = hoffman ;
    %First1 = morgan,
    %Last1 = rielly,
    %City = tor,
    %First2 = john,
    %Last2 = tavares ;
    %First1 = patrick,
    %Last1 = kane,
    %City = chi,
    %First2 = alex,
    %Last2 = debrincat ;
    %false.


%What players have more than 100 points? (where points = goals + assists)
%player(name(First,Last),_,_,stats(Goals,Assists,_)),(Goals + Assists)>100.

    %Output:
    %First = leon,
    %Last = driasaitl,
    %Goals = 50,
    %Assists = 55 ;
    %First = nikita,
    %Last = kucherov,
    %Goals = 41,
    %Assists = 87 ;
    %First = patrick,
    %Last = kane,
    %Goals = 44,
    %Assists = 66.

%What is the shot accuracy of the player with the most goals? (where shot accuracy = goals / shots)
%player(name(First,Last),_,_,stats(Goals,_,Shots)), not((player(name(First2,Last2),_,_,stats(Goals2,_,Shots2)), Goals2>Goals)),Accuracy is (Goals / Shots).

    %Output:
    %First = alex,
    %Last = ovechkin,
    %Goals = 51,
    %Shots = 338,
    %Accuracy = 0.15088757396449703


%Who is the least accurate left wing (lw) player?
%player(name(First,Last),_,pos(lw),stats(Goals,_,Shots)), not((player(name(First2,Last2),_,pos(lw),stats(Goals2,_,Shots2)), ((Goals2/Shots2)<(Goals/Shots)))),Accuracy is (Goals / Shots).

    %Output:
    %First = kevin,
    %Last = fiala,
    %Goals = 13,
    %Shots = 174,
    %Accuracy = 0.07471264367816093
