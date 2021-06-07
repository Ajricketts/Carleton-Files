// file is sum_threads.c
/********************************************************************/

/* 
Purpose: demonstrates reace condition of a critical code

The program attempts to mimic processing 50,000 records and store the result in a single global variable.

The simulation is done by computing the sum of numbers 1-50000 as (1+2+...+50000) where each addtion 
takes about 200 micro seconds.  The progam uses five threads to complete the work where 
each thread is responsible for computing a subset of the numbers (e.g., thread 1 would compute the sum
1 - 10000, thread 2 would compute the sum of number 10001-20000 and so on).    

The progam show that the sum is not computed correctly as there is a race between the threads when
updating the global variable totalSum  


*/



/****************************************************************/
// Includes

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>


/***************************************************************/
// Structures


// holds the task informaotin for each process
typedef struct threadData { 
    int tid;			// thread id
    unsigned long start;	// start range
    unsigned long end;		// end range
} THREAD_DATA; 


/******************************************************************/
// Define


#define NUM_THREADS 5
#define BLOCK_SIZE  10000


/******************************************************************/
// Function Prototypes

void *printSum(void *ptr);		

/***************************************************************/
// Global Variables
unsigned long totalSum = 0;		// global value that holds the final result
int start = 0;					// a global variable for ensuring the all threads start at the same time.

/*************************************************************/

int main(int argc, char ** argv)
{
    pthread_t tid[NUM_THREADS];
    int  i, rc; 
    THREAD_DATA tdata[NUM_THREADS];		// holds the tasks for each thread

	
    totalSum = 0;		// init the global results

	// assign work for each thread and create a thread
    for (i = 0; i<NUM_THREADS; i++) {
        tdata[i].tid = i;
        tdata[i].start = i * BLOCK_SIZE +1;
        tdata[i].end = (i+1) * BLOCK_SIZE;

        printf("create thread %d \n",i);
        rc = pthread_create(&tid[i], NULL, printSum, (void *)&tdata[i]);
        if (rc) {
            fprintf(stderr, "Error - pthread_create() return code: %d\n", rc);
            exit(1);
        }
    }

	// set start to 1 so that all treads will start the processing at the same time
	start = 1;

	// wait for the threads to terminate
    for (i = 0; i < NUM_THREADS; i++) pthread_join(tid[i], NULL);

	// print the global sum
    printf("sum = %lu \n",totalSum);

}


/***************************************************************************/
/* Purpose compute the sum in the range and store it in the global variable totalSum


input:
ptr - date of the task that was set for the thread

output
none

return 
none

*/


void *printSum(void *ptr)
{
    THREAD_DATA *data;
    data = (THREAD_DATA *) ptr;
    int localSum = 0;
	int i; 

	// loop until the start
    while (!start);	
    
	for (i = data->start; i <= data->end; i++)  {

		// do the computation
        localSum = totalSum;
        usleep(50);       
        totalSum = localSum + i;
		
		usleep(100);       

    }

    printf("tid[%d] finished range = %lu  - %lu \n", data->tid, data->start, data->end);
}


