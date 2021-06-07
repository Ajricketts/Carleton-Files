#ifndef COURSE_H
#define COURSE_H

class Course
{
  public:
    Course(int=0, int=0, int = 0, string = "");
    void print();

  private:
    int code;	// course code, for example 2404 for COMP2404
    int grade;	// numeric grade from 0 (F) to 12 (A+), with -1 for WDN
    int termTaken; // The term the course was taken, using the Carleton university
                   //   standard YYYYTT, where YYYY is the four-digit year and TT
                   //   reprosents the term, 10 for winter, 20 for summer, 30 for fall
    string instructor; // The course instructor, for example "Dr. Christine Laurendeau"
    void getGradeStr(string&);
};

#endif
