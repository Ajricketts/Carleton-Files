#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

#include "Student.h"

Student::Student(int i)
{
  id = i;
  numCourses = 0;
}

void Student::setId(int i)
{
  id = i;
}

void Student:: setCourse(int i, int j, int k)
{
}
void Student::print()
{
  cout<< endl << "Id: " << id << endl;

  for (int i=0; i<numCourses; ++i)
    courses[i] -> print();
}

void addCourse(Course* c) 
{
	courses[numCourses] = c;
	numCourses++;
}

Student::~Student() 
{
	delete []courses;
}
