#ifndef STUDENT_H
#define STUDENT_H

#include "defs.h"
#include "Course.h"

class Student
{
  public:
    Student(int=0);
    ~Student();
    void setId(int);
    void setCourse(int, int, int);
    void setNumCourses(int);
    void print();

  private:
    int    id;
    Course* courses;
    courses = new Course [MAX_NUM_COURSES];
    int    numCourses;
};

#endif
