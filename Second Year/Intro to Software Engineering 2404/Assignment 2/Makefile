sas:	main.o Student.o Course.o Storage.o View.o
	g++ -o sas main.o Student.o Course.o Storage.o View.o

main.o:	main.cc Storage.h defs.h View.h
	g++ -c main.cc

View.o: View.cc View.h defs.h
	g++ -c View.cc

Student.o:	Student.cc Student.h Course.h defs.h
	g++ -c Student.cc

Course.o:	Course.cc Course.h
	g++ -c Course.cc

Storage.o:	Storage.cc Student.h Storage.h defs.h
	g++ -c Storage.cc

clean:
	rm -f *.o sas
