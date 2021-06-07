#ifndef STUDENT_H
#define STUDENT_H

#include "defs.h"
#include "Course.h"

class Student
{
  public:
    Student(int=0);
    ~Student();
    void print();
    void addCourse(Course*);

  private:
    int    id;
    Course* courses[MAX_NUM_COURSES];
    int    numCourses;
};

#endif
