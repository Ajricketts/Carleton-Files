Threads

Three files are given as code examples for using threads:
1. spawn_thread.c – this file provides a simple example of creating threads by the main program and then waiting until the threads completed their work.  Here each thread is using the same startup function.

2. sum_thread.c – this file shows how threads can be allocated separate tasks using data that is past in as start up information (similar to the argc, and argv that are passed into main).   Here, all threads execute the same code on different data.  

Note that the result of the execution of the threads is not correct because there is a race between the threads to write to the single global variable.

3. sum_thread_mutex.c – this example shows how the race problem in sum_thread.c can be averted using mutual exclusion.  Mutual exclusion (mutex) ensures that critical section of the code is used exclusively by the thread. 

Compiling 
To compile and execute the code one needs to use the thread library pthread.

Command example:  gcc spawn_thread.c -lpthread
