%This predicate will sum a range of values between two parameters
%sum_range(Start,End,Result).

%base case
%sum_range(A,B,Result):- A==B, A=Result.
sum_range(A,A,A).   %alternate version


%recursive
sum_range(A,B,Result):-
	A1 is A+1,
	sum_range(A1,B,Result1),
	Result is Result1+A.
	
	


fib(N,R):-
	N>=2,
	N1 is N-1,
	N2 is N-2,
	fib(N1,R1),
	fib(N2,R2),
	R is R1+R2.
	
fib(0,0).
fib(1,1).

%0! = 1
%n! = n*(n-1)!
factorial(0,1). % 0! = 1
factorial(N,F):-
      N > 0,
      N1 is N - 1,
      factorial(N1, F1),
      F is N * F1.
	  
	  
facit(N,F):- factorial(0,N,1,F).
factorial(N,N,T,T). %base case
factorial(I,N,T,F):-
      I < N,
      I1 is I + 1,
      T1 is T * I1,
      factorial(I1,N,T1,F).
	  
	  
facit2(N,F):- factorial(N,1,F).
factorial(0,F,F).
factorial(N,T,F):-
	N>0,
	N1 is N-1,
	T1 is T * N,
	factorial(N1,T1,F).
	
fibit(N,R):- fibit(N,1,0,R).
fibit(1,R,_,R).
fibit(N,FibN1,FibN2,R):-
	N>1,
	Fib is FibN1+FibN2,
	N1 is N-1,
	fibit(N1,Fib,FibN1,R).
