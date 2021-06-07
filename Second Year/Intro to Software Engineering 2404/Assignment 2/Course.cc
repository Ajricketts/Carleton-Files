#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

#include "Course.h"

Course::Course(int c, int g, int t, string i)
{
  // Initialize all variables needed
  code  = c;
  grade = g;
  termTaken = t;
  instructor = i;
}

void Course::print()
{
  string str;

  // Print the all the course information to the console
  //  this inclueds the course code, grade acheived, term the course was Taken
  //  and the instructor who tought the course

  cout << "-- COMP " << code << ":  ";
  cout << right << setw(2) << grade   << "  ";
  getGradeStr(str);
  cout << left << setw(3) << str;
  cout << right << setw(2) << termTaken   << "  ";
  cout << instructor << "  " << endl;


}

void Course::getGradeStr(string& gradeStr)
{
  //Get the letter grade based on the number grade they achieved

  string gradeStrings[] = {
    "WDN", "F", "D-", "D", "D+", "C-", "C", "C+",
    "B-", "B", "B+", "A-", "A", "A+" };

  if ( grade >= -1 && grade <= 12 )
    gradeStr = gradeStrings[grade+1];
  else
    gradeStr = "Unknown";
}
