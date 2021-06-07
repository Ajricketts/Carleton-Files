%employee(ID, name(Last,First), address(Num,Street,City), Salary, date_of_birth(Day,Month,Year)).

employee(20163, name(smith, john), address(35, king_street, ottawa), 40000, date_of_birth(30, 9, 1973)).

employee(20164, name(palmer, david), address(26, queen_street, ottawa), 45000, date_of_birth(12, 1, 1982)).

employee(20165, name(ray, anna), address(1234, open_street, nepean), 50000, date_of_birth(1, 1, 1975)).

employee(20166, name(ray, billy), address(1234, open_street, nepean), 45000, date_of_birth(1, 1, 1954)).

employee(20167, name(black, edward), address(62, small_drive, hull), 68000, date_of_birth(31, 12, 1968)).

employee(20168, name(norman, robert), address(25, parkway, ottawa), 68000, date_of_birth(15, 10, 1979)).

employee(20169, name(smith, maggie), address(35, queen_street, ottawa), 55000, date_of_birth(15, 10, 1979)).

employee(20170, name(tsume, sarah), address(708, bank_street, ottawa), 65500, date_of_birth(21, 5, 1985)).




%Some practice queries:

%What are the details of employee #20165?
% ?- employee(20165,Name,Address,Salary,DoB).

%Is Anna Ray an employee?
% ?- employee(_,name(ray,anna),_,_,_).

%Retrieve just the first name of employee 20163?
% ?-  employee(20163,name(_,FirstName),_,_,_).

%What's the salary of john smith?
% ?-employee(_,name(smith,john),_,Salary,_).

%Who lives in ottawa?
% ?-  employee(_,name(Last,First),address(_,_,ottawa),_,_).

%Name(s) of employee(s) born in january?
% ?- employee(_,Name,_,_,DoB), DoB=date_of_birth(_,1,_).

%Any two employees live on the same street?
% ?- employee(Id1,Name1,address(_,Street,_),_,_),employee(Id2,Name2,address(_,Street,_),_,_),not(Id1=Id2).