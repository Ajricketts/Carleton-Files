/* File is main.c
 *
 * Purpose: 
 * test the function convert.c
 *
 Revision history

 September 2018 - Created 

    copyright Doron Nussbaum 2018
    do not distribute

 */

#include "stdio.h"
#include "convert.h"


int main(int argc, char **argv)

{
    int num = 7;
    int base = 2;

    printf("Testing the convert() function \n");

    // testing base 2
    base = 2;
    num = 11;
    printf("%d in base %d is ",num,base);
    convert(num,base);
    printf("\n");

    num = 5357;
    printf("%d in base %d is ",num,base);
    convert(num,base);
    printf("\n");
    
    // testing base 8
    base = 8;
    num = 11;
    printf("%d in base %d is ",num,base);
    convert(num,base);
    printf("\n");

    num = 5357;
    printf("%d in base %d is ",num,base);
    convert(num,base);
    printf("\n");
    return(0);
}


