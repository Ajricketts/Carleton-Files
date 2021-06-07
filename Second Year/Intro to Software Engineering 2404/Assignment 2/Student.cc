#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

#include "Student.h"
#include "View.h"

Student::Student(int i)
{
  // Initialize all variables needed.
  id = i;
  numCourses = 0;
}

void Student::addCourse(Course* c)
{
  if (numCourses >= MAX_NUM_COURSES)
  {
      // check if the maximum number of courses has been reached
      //  and notify the user if it has
      cout << "Max number of courses reached" << endl;
      return;
  }
  courses[numCourses] = c; // add the course to the array
  ++numCourses; // increase the number of courses added
}

void Student::print()
{
  cout << "Reached";
  cout<< endl << "Id: " << id << endl;

  for (int i=0; i<numCourses; ++i)
    courses[i] -> print(); // Print each course out to the console using the print
                           //   function in the courses class
}

Student::~Student()
{
  for (int i = 0; i < numCourses; ++i)
  {
    delete courses[i]; // Loop through the array and free up all the allocated memory
  }
}
