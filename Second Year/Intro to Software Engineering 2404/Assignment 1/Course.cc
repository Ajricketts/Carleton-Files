#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

#include "Course.h"

Course::Course(int c, int g, int t, string i)
{
  code  = c;
  grade = g;
  courseTaken = t;
  instructor = i;
}

void Course::print()
{
  string str;

  cout << "-- COMP " << code << ":  ";
  cout << right << setw(2) << "Instructor: " << instructor;
  cout << "Taken: " << courseTaken;
  cout << grade   << "  ";
  getGradeStr(str);
  cout << left << setw(3) << str << endl;

}

void Course::getGradeStr(string& gradeStr)
{
  string gradeStrings[] = {
    "WDN", "F", "D-", "D", "D+", "C-", "C", "C+", 
    "B-", "B", "B+", "A-", "A", "A+" };

  if ( grade >= -1 && grade <= 12 )
    gradeStr = gradeStrings[grade+1];
  else
    gradeStr = "Unknown";
}

