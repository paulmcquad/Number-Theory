// Description: Print all the prime factors of a given number.
// Author     : Paul McQuade <paulmcquad@gmail.com>
// License    : GPLv3

#include <stdio.h>
#define Until(COND) while(!(COND))

int main(int argc, char const *argv[])
{
	int n, i, fm;

    printf("n = ");
    scanf("%d", &n);

    i = 2;
    do {
        fm = 0;
        while(n % i == 0) {
            fm++;
            n /= i;
        }
        if( fm ) printf("%d^%d ", i, fm);
        i++; 

    } Until( (n == 1) );
    
	return 0;
}