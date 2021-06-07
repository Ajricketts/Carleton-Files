/* 
File is singleSpawn.c

Purpose:
The program forks into a parent and a child, reads an unsigned int from a binary file and then morphs the child into the isPrime program to check if said number is a prime number or not. The parent then takes the return value from the child and prints to the terminal if the input number is a prime number or not

input:
binary file - A binary file that includes at least one unsigned integer         

output:
2 - if the command line parameter is not correct 
3 - if the file provided does not exist
- If the input number is a prime number
- If the input number is not a prime number

Assumption:
As with the isPrime program, the program does not check if the number is a positive integer         

*/

/**************************************************************/
// INCLUDE FILES
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

/*************************************************************/
// PROTYPES
//
int morph(char *number);
pid_t wait(int *wstatus);

/************************************************************/

int main(int argc, char *argv[]) {                                                                  
    int rc;
    FILE *filestream;                                                           
    unsigned int fInt = 0;                                                  
    char *buffer;
    int wstatus;
    int pid = fork();
    pid_t cpid;

    cpid = wait(&wstatus);           
        
    // Check to see if the user provided a second argument to the terminal      
    if (argc < 2) {                                                             
        printf("Usage: singlePrime %s \n", argv[1]);                            
        return(2); //Return 2 if a file name is not provided                    
    }                                                                                                                                                           
    // Check if file exists                                                                         
    if (access(argv[1], F_OK) == -1) {                                      
        printf("file %s doesnot exist", argv[1]);                           
        return(3);                                                              
    }                                                                           
    
    else {                                                          
        // Open the binary file in read mode                                    
        filestream = fopen(argv[1], "rb");                                                                                                                  
        // Read first unsigned int from binary file                             
        fread(&fInt, sizeof(unsigned int), 1, filestream);                  
        sprintf(buffer, "%d", fInt);                                                                                                            
        // Morph child process into isPrime
        if (pid == 0)  {
            morph(buffer);
        }
        
        // Parent Process Instructions
        // Parent process waits for the return value of the child process and then prints if the number was prime or not
        
        else if (WEXITSTATUS(wstatus) == 2) {
            printf("FAILED"); //If 2 is returned the process has failed

        }

        else if (WEXITSTATUS(wstatus) == 1) {
            // If 1 is returned the input number is a prime number
            printf("The input number: %s is a prime number", buffer);

        }

        else if (WEXITSTATUS(wstatus) == 0) {
            // If 0 is returned the input number is not a prime number    
            printf("The input number: %s is not a prime number", buffer);    
         
        }      
    }       
}                                                                                                                                                     
int morph(char *number) {                                                       
    int i;                                                                  
    char *args[] = {"./isPrime", number, NULL};                                 
    execvp(args[0], args);    
}    
