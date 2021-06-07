#ifndef VIEW_H
#define VIEW_H

#include "defs.h"
#include "Student.h"

class View
{
  public:
    View();
    //~View();
    int mainMenu();
    void readId(Student*);
    //void readCourse();
    //void print();

  private:
    //Student* tempStu;

};


#endif
