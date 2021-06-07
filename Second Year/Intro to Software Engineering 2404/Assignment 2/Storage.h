#ifndef STORAGE_H
#define STORAGE_H

#include "defs.h"
#include "Student.h"

class Storage
{
  public:
    Storage(); // Default constructor
    ~Storage(); // Decunstructor to free up all the allocated memory
    void print(); // Print all the students to the console
    void addStu(Student*); // Add a student to the array of pointers

  private:
    Student* students[MAX_NUM_STU]; // Define an array of student pointers
    int    numStudents; // Keep track of the number of students
};

#endif
