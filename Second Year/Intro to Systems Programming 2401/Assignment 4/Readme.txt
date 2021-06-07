Developer: Alyxander-Jacob Ricketts      Development Date: Friday December 7th 2018 

Purpose:
        For singlePrime.c:  The program reads an unsigned int from a binary file and then morphs into the isPrime program to check if said number is a prime number or not

        For singleSpawn.c:  The program forks into a parent and a child, reads an unsigned int from a binary file and then morphs the child into the isPrime program to check if said number is a prime number or not. The parent then takes the return value from the child and prints to the terminal if the input number is a prime number or not

        For multiSpawn.c:  The program forks into a parent and multiple children, reads all unsigned ints from a binary file, and stores the children process Ids and then morphs the children into the isPrime program to check if the number associated with that child is a prime number or not. The parent then takes the return value from the children and only returns the prime numbers

        For multiSignalSpawn.c:  The program forks into a parent and multiple children, reads all unsigned ints from a binary file, and stores the children process Ids and then morphs the children into the isPrime program to check if the number associated with that child is a prime number or not. The parent then takes the return value from the children and only returns the prime numbers. If you kill the processes using the kill - SIGUSR1 Process Id the program will output the number of processes completed and the number of processes still running
 


List of Source Files: isPrime.c, createBinary.c, singlePrime.c, singleSpawn.c, multiSpawn.c, Makefile1, Makefile2, Makefile3, prime.bin, prime.txt, isPrime, singleMorph, singleSpawn, multiSpawn, multiSignalSpawn.c, Readme.txt 


Compilation Command: 
        For singlePrime.c: gcc -o singleMorph singlePrime.c 
        
        For singleSpawn.c: gcc -o singleSpawn singleSpawn.c

        For multiSpawn.c: gcc -o multiSpawn multiSpawn.c

        For multiSignalSpawn.c: gcc -o multiSignalSpawn multiSignalSpawn.c

Launching and operating instructions: Compile the code using one of the compilation commands above in terminal. Provide the program with a binary file with at least one unsigned int in it. 

Example: When running the program multiSpawn.c with the compilation command given above, and the prime.bin file included with the program, the output should read these numbers in no given order:

        13417 is a prime number
        35788631 is a prime number
        199905059 is a prime number
        200003627 is a prime number
        299905657 is a prime number
        299902243 is a prime number
        961751257 is a prime number

        

Issues/Limitations: A limitation of these programs is that they assume that the user is not giving them a negative number.

