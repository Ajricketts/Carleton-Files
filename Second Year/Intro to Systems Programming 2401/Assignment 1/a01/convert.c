/* file is convert.c 

   copyright Doron Nussbaum 2018
   do not distribute
*/

#include "stdio.h"
#include "convert.h"

/* converts a decimal number to a representation in another base
 * and prints the number in the new base
 *
 * input:
 * num - the number in decimal
 * base - the base to which num has to be converted to
 *
 * output:
 * none
 *
 */

int convert(int num, int base)

{
    int remainder = num % base;
    if (num == 0) {
	return(0);
    }
    convert((num / base), base);

    printf("%d", remainder);

}
