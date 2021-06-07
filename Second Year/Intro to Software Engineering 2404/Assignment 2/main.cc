#include <iostream>
using namespace std;
#include <string>

#include "defs.h"
#include "Student.h"
#include "Storage.h"
#include "View.h"

int  mainMenu();


int main()
{
  View    view;
  Storage storage;
  int     numStu = 0;
  int     stuId;
  int     courseCode, grade, term;
  int     menuSelection;
  string  instructor;

  Student* tempStu;
  Course*  tempCourse;

  while (1) {
    menuSelection = view.mainMenu();

    if (menuSelection == 0)
      break;

    else if (menuSelection == 1) {

      view.readId(tempStu);
      tempStu -> print();

      while (1) {
        cout << "course code <0 to end>:  ";
        cin  >> courseCode;
        if (courseCode == 0)
          break;
        cout << "grade:                   ";
        cin  >> grade;

        cout << "Term Taken (In the format of YYYYTT):                 ";
        cin >> term;

        cout << "Instructor:                 ";
        cin >> instructor;

        tempCourse = new Course(courseCode, grade, term, instructor);
        tempCourse -> print();
        //tempStu -> addCourse(tempCourse);

      }
      storage.addStu(tempStu);
      ++numStu;
    }
  }

  if (numStu > 0)
    storage.print();

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
