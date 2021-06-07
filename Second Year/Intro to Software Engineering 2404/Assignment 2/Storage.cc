#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

#include "Storage.h"

Storage::Storage()
{
  numStudents = 0;
}

void Storage::addStu(Student* s)
{
  if (numStudents >= MAX_NUM_STU)
  {
      // check if the maximum number of students has been reached
      //  and notify the user if it has
      cout << "Max number of students reached";
      return;
  }
  students[numStudents] = s; // add the student to the array
  ++numStudents; // increase the number of studnets added
}

void Storage::print()
{
  for (int i=0; i<numStudents; ++i)
    students[i] -> print(); // Print each student out to the console using the print
                           //   function in the student class (therefore using the function in the course class)
}

Storage::~Storage()
{
  for (int i = 0; i < numStudents; ++i)
  {
    delete students[i]; // Loop through the array and free up all the allocated memory
  }
}
