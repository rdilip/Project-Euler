#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void ptPrint (long M[], long len);

void mark(int *sieve, int len, int x) {
	int i;
	for (i = x + x; i < len; i += x) {
		*(sieve + i) = 0;
	}
}

/** Creates the sieve, non inclusive
 * First value is the number of elements represented 
 */

int *primeSieve(int limit) {
	int *M = malloc(sizeof(int));
	int i, count;
	long lower = (long)(sqrt(limit)) + 1;

	for (i = 0; i < limit; i++) {*(M + i) = 1;}

	for (i = 2; i < lower; i++) {
		mark(M, limit, i);
	}
	
	*M = 0;
	*(M + 1) = 0;

	count = 0;
	for (i = 0; i < limit; i++) {
		if (*(M + i)) {
			count++;
		}
	}
	*M = count;

	return (M);
	free(M);
}

void ptPrint (long *M, long len) {
	long i;
	for (i = 0; i < len; i++) {
		printf("%ld: %ld\n", i, *(M + i));
	}
}


