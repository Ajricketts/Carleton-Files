%build rules
slowRule(X,Y):- firstPart(X), secondPart(Y), pairsWith(X,Y).
fastRule(X,Y):- secondPart(Y), firstPart(X), pairsWith(X,Y).
fasterRule(X,Y):-pairsWith(X,Y),firstPart(X),secondPart(Y).

firstPart(X):- part(X).
secondPart(X):- part(X),write("Evaluating....\n"),flush_output,sleep(2).

%parts in stock
part(a).
part(b).
part(c).
part(d).

%parts that work together
pair(a,z).
pair(a,y).
pair(a,x).
pair(b,q).
pair(c,b).
pair(y,c).
%pair(X,Y):-pair(Y,X).   %symmetric?

pairsWith(X,Y):-pair(X,Y).  %symmetric
pairsWith(X,Y):-pair(Y,X).


%pair(X,Y):-pair(X,Temp),pair(Temp,Y).   %transitive?

%?-pair(a,b).
%pair(a,Temp),pair(Temp,b).
%pair(z,b).
%pair(z,Temp),pair(Temp,b).
%pair(z,Temp'),pair(Temp',Temp),pair(Temp,b).
%pair(z,Temp''),pair(Temp'',Temp'),pair(Temp',Temp),pair(Temp,b).
%...

pairsWith(X,Y):-pair(X,Temp),pairsWith(Temp,Y).



