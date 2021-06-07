
/*

File bit_manipulation.h

Purpose:header file of functions prototypes

*/

/************************************************************************/

// INCLUDE FILES


#include "stdio.h"
#include "stdlib.h"
#include "assert.h"


/************************************************************************/
// FUNCTION PROTOTYPES

void rotateLeft(char *c, int numBits);
void rotateRight(char *c, int numBits);
void translateChar(char *c, char key, int index);
void revTranslateChar(char *c, char key, int index);
int encryptChar(char *c, char key, int index);
int decryptChar(char *c, char key, int index);
int countBits(char c);


