
/*

File bit_manipulation.c

Purpose :
contains helper functions for manipulating bits


Revisions:
file created: Doron Nussbaum

*/

/************************************************************************/

// INCLUDE FILES

#include "bit_manipulation.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "assert.h"

/************************************************************************/
//MACROS  / DEFINES



/************************************************************************/
// FUNCTION PROTOTYPES
int encryptChar(char *c, char key, int index);
void rotateLeft( char *c, int numBits);
void rotateRight( char *c, int numBits);
void translateChar(char *c, char key, int index);
void revTranslateChar(char *c, char key, int index);
int countBits(char c);
int decryptChar(char *c, char key, int index);





/*************************************************************************************/
/* purpose: perform circular rotation to the left by numBits

input:
c - the character to be checked
numBits - how many bits need to be rotated

return:
none

*/

void rotateLeft( char *c, int numBits)

{
	// add code
	// shifting charecters to the left
	*c = ((unsigned char)*c << numBits) | ((unsigned char)*c >> (8 - numBits));
}



/*************************************************************************************/
/* purpose: perform circular rotation to the right by numBits

input:
c - the character to be checked
numBits - how many bits need to be rotated

return:
none

*/

void rotateRight(char *c, int numBits)

{
    // add code
    // shifting characters to the right

    *c = ((unsigned char)*c >> numBits) | ((unsigned char)*c << (8 - numBits));


}

/*************************************************************************************/

/* purpose: translate the value of by a certain amount

input:
c - the character
key - is the key for the encryption
index - is the index of the character in the array

output:
c - the character

return:
None

Description:
This function translate the value of c by a computed amount.
The translate can be done by adding "amount" to c.

The amount is computed using the the key, the index, and the
value of *c.
the formula is
 the value of the character + (57 * index + key)

Example 1:
Assume that *c is 65 (0x41), key is 87 and index is 1.

65 + 57 * 1 + 87.


*/
void translateChar(char *c, char key, int index)

{
	// add code
	// set the pointer to c to the translated value
	*c = *c + ((57 * index) + key);
}



/*************************************************************************************/

/* purpose: rev the translate the value of by a certain amount

Description:
This function translate the value of c by a computed amount.
The translate can be by adding "amount" to c.

The amount is computed using the the key, the index, and the
value of *c.
the formula is
the value of the character - (57 * index + key)

Example 1:
Assume that *c is 65 (0x41), key is 87 and index is 1.

65 - (57 * 1 + 87).


*/
void revTranslateChar(char *c, char key, int index)
{
	// add code
	// set the pointer to c to the reverse of the translated value
        *c = *c - ((57 * index) + key);

}





/*************************************************************************************/


/*  count the number of bits in a short

input:
num - a short integer

return
the number of bits that are set to 1 in num



*/
int countBits(char c)

{

    // add code

    int value = c;
    int count = 0;
    while (value != 0) {
        value = value & (value - 1);
        count++;
    }
    return count;
}






/*************************************************************************************/


/* Purpose: encrypt a character

input:
*c - the character to encrypt
key - the encryption key
index - the index of the character in the array

output:
*c - the encrypted character

return
0



*/
int encryptChar(char *c, char key, int index)

{

	int numBits = 0;

	// translate the character
	translateChar(c, key, index);

	// calculate the number bits to rotate
	int rotateNum = (index + countBits(*c)) % 8;

	// perform circular rotation of the char
	if (countBits(*c) % 2 != 0) {
 	    rotateRight(c, rotateNum);
	}

	else {
	    rotateLeft(c, rotateNum);
	}
	// xor the char
	*c = *c ^ key;

	return(0);


}


/*************************************************************************************/


/* Purpose: decrypt a character

input:
*c - the character to encrypt
key - the encryption key
index - the index of the character in the array

output:
*c - the encrypted character

return
0



*/
int decryptChar(char *c, char key, int index)
{
	// xor the char
	*c = *c ^ key;
	// calculate the number of bits to rotate
	int rotateNum = (index + countBits(*c)) % 8;

	// perform circular rotation of the char
	if ((countBits(*c) % 2) == 0) {
	    rotateRight(c, rotateNum);
	}
	else {
	    rotateLeft(c, rotateNum);
	}
	// translate the character
	revTranslateChar(c, key, index);
	return(0);


}
