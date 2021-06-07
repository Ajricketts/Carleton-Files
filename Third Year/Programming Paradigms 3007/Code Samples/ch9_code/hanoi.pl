%simulates the towers of hanoi problem for n discs on 3 pegs
%hanoi(Src,Aux,Dest,N).

%base case
hanoi(Src,_,Dest,1):-
	write(Src),
	write(" -> "),
	write(Dest),
	nl.
	
hanoi(Src,Aux,Dest,N):-
	N1 is N-1,
	hanoi(Src,Dest,Aux,N1),
	hanoi(Src,Aux,Dest,1),
	hanoi(Aux,Src,Dest,N1).

