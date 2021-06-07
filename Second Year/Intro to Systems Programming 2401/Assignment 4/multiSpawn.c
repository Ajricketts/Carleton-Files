/*                                                                              
File is multiSpawn.c                                                           

Purpose:                                                                        

The program forks into a parent and multiple children, reads all unsigned ints from a binary file, and stores the children process Ids and then morphs the children into the isPrime program to check if the number associated with that child is a prime number or not. The parent then takes the return value from the children and only returns the prime numbers

input:                                                                          
binary file - A binary file that includes at least one unsigned integer         

output:   
2 - if the command line parameter is not correct                                
3 - if the file provided does not exist                                         
- prints only the prime numbers to the terminal                             

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
/*********:****************************************************/                                     
// PROTYPES                                                             
//                                                                              
int morph(char *number);                                                        
pid_t wait(int *wstatus);                                                                                                                                       
/************************************************************/                  

int main(int argc, char *argv[]) {                                          
    
    int rc;                                                                 
    FILE *filestream;                                                      
    char *buffer;                                
    int wstatus;
    int pid;    
    int childPid = 0;
    int size;    
    
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
        fseek(filestream, 0, SEEK_END); // Move file pointer to the end of the file
        size = ftell(filestream) / 4; // Get the size of the file
        rewind(filestream); // Move the file pointer back to the beginning of the file
        
        unsigned int fInt[sizeof(unsigned int) * size];
        unsigned int childProcessIds[size];
         
        // Read all unsigned ints from binary file                             
        fread(&fInt, sizeof(unsigned int), size, filestream);        
        fclose(filestream);
        // Fork into a child process as many times as the number of unsigned ints
        for (int i = 0; i < size; i++) {
            
            int pid = fork();
            char *buffer = malloc(size); // Allocate memory for the buffer
            sprintf(buffer, "%d", fInt[i]); // Change each unsigned int into a char

            if (pid == 0) {
               morph(buffer); // Morph each child into the isPrime program
            }
            
            else if (pid != 0){
                childProcessIds[i] = pid; // Store the child process Id
               
            }
        }
        

        // Loop until there are no more child processes left        
        while ((pid = waitpid(-1, &wstatus, 0)) != -1) {
            
            if (WEXITSTATUS(wstatus) == 1) { // If the child process Exited with a status of 1 (The number is a prime number)
                int count = 0;
    
                for (int j = 0; j < size; j++) { // Find the index of the number as the child 
                                                 //  processes and numbers are stored in their respective arrays at the same index
                    count++;
                    if (pid == childProcessIds[j]) {
                        printf("%u is a prime number\n", fInt[count - 1]); // Print the prime numbers only
                    }
                }
                
            }
        }

    }                                                                           
}                                                                           
int morph(char *number) {                                                   
    // Function to morph into the isPrime program                                 
    char *args[] = {"./isPrime", number, NULL};                                 
    execvp(args[0], args);                                                  
}  
