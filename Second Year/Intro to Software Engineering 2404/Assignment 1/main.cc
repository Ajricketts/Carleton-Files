#include <iostream>
using namespace std;
#include <string>

#include "defs.h"
#include "Student.h"

int  mainMenu();
void printStorage(Student stuArr[MAX_NUM_STU], int);


int main()
{
  Student students[MAX_NUM_STU];
  int     numStu = 0;
  int     numCourses;
  int     stuId, courseCode, grade;
  int     menuSelection;

  while (1) {
    menuSelection = mainMenu();

    if (menuSelection == 0) 
      break;

    else if (menuSelection == 1) {

      cout << "student id:   ";
      cin  >> stuId;
      students[numStu].setId(stuId);
      numCourses = 0;

      while (1) {
        cout << "course code <0 to end>:  ";
        cin  >> courseCode;
        if (courseCode == 0)
          break;
        cout << "grade:                   ";
        cin  >> grade;

        students[numStu].setCourse(numCourses, courseCode, grade);
        ++numCourses;
      }
      students[numStu].setNumCourses(numCourses);
      ++numStu;
    }
  }

  if (numStu > 0)
    printStorage(students, numStu);

  return 0;
}

int mainMenu()
{
  int numOptions = 1;
  int selection  = -1;

  cout << endl;
  cout << "(1) Add student" << endl;
  cout << "(0) Exit" << endl;

  while (selection < 0 || selection > numOptions) {
    cout << "Enter your selection: ";
    cin  >> selection;
  }

  return selection;
}

void printStorage(Student stuArr[MAX_NUM_STU], int numStu)
{
  cout << endl << endl << "STUDENT INFO: " << endl;

  for (int i=0; i<numStu; ++i)
    stuArr[i].print();

  cout << endl;
}

