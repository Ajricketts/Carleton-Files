/* 
File is singlePrime.c

Purpose:
The program reads an unsigned int from a binary file and then morphs into the isPrime program to check if said number is a prime number or not

input:
binary file - A binary file that includes at least one unsigned integer         

output:
2 - if the command line parameter is not correct 
3 - if the file provided does not exist

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

/*************************************************************/
// PROTYPES
//
int morph(char *number);


/*************************************************************/


int main(int argc, char *argv[]) {
    int rc;
    FILE *filestream;
    unsigned int fInt = 0;
    char *buffer;

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
       
        // Morph program into isPrime
        morph(buffer);
    }

}

int morph(char *number) {
    int i;
    char *args[] = {"./isPrime", number, NULL}; 
    execvp(args[0], args);
}


