#ifndef COURSE_H
#define COURSE_H

class Course
{
  public:
    Course(int=0, int=0);
    void setCode(int);
    void setGrade(int);
    void print();

  private:
    int code;	// course code, for example 2404 for COMP2404
    int grade;	// numeric grade from 0 (F) to 12 (A+), with -1 for WDN
    void getGradeStr(string&);
};

#endif
