#include <iostream>
using namespace std;
#include <string>
#include <iomanip>

#include "defs.h"
#include "View.h"
#include "Student.h"

View::View()
{

}

int View::mainMenu()
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

void View::readId(Student* tempStu)
{
  int tempStuId = 0;
  cout << "student id:   ";
  cin  >> tempStuId;
  cout << tempStuId;
  tempStu = new Student(tempStuId);

}
