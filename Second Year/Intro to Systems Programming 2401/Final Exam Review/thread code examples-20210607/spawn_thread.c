// file is sum_threads_mutex.c
/********************************************************************/

/* 
Purpose: demonstrates spawing of threads 

The program spanws two threads each printing a different message 


*/



/****************************************************************/
// Includes

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

/******************************************************************/
// Function Prototypes


void *printMsg(void *ptr);


/******************************************************************/


int main(int argc, char **argv)
{
	pthread_t tid[2];		// thread handles
	const char *msg[2]={"thread 1: Hello World!","\t\t thread 2: Hello Again!"}; 
	int rc; 
    int i;

	/* Create independent threads each of which will execute function */

    for (i = 0; i < 2; i++) {
        rc = pthread_create(&tid[i], NULL, printMsg, (void*)msg[i]);
	    if (rc) {
		    fprintf(stderr, "Error - pthread_create() return code: %d\n", rc);
		    exit(1);
        }
	}


	/* Wait till threads have computed their task before main continues.*/
	/* Othewise there is a risk of main exiting which will terminate   */
	/* the program before the threads have completed their tasks.   */

    for (i = 0; i < 2; i++) {
       pthread_join(tid[i], NULL);
    }
    printf("main before exit \n");
    sleep(4);
	exit(0);
}


/******************************************************/
// Purpose: prints a message 
void *printMsg(void *ptr)
{
	char *message = (char *)ptr;
    usleep(5000);
    printf("%s \n", message);
 
}

