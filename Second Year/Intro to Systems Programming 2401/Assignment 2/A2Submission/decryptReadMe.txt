Author: Alyxander-Jacob Ricketts

Purpose: A program that allows you to enter a encrypted message and decrypt it. The decryption proccess involves a xor operation,circular rotation, and charecter shifting using a key (Caesar Cypher).                 

List of Source Files: decrypt.c, bit_manipulation.h, bit_manipulation.c, decryptReadMe.txt

Compilation Command: gcc -o decrypt decrypt.c bit_manipulation.c

Launching and operating instructions: Compile the code using the compilation command above in terminal. Using the program type in the encrypted message you wish to decrypt. Then put in the key (the key the encrypted message was encrypted with) and the output will be your decrypted message.

Example: Input this into the decrypt function: 10 -76 -58 34 -6 8 80 -99 -104 -79 59 81 47 2 1 47 -14 37 65 -92 110 -75 6 112 51
                                               The output should be: "This was a fun assignment"
