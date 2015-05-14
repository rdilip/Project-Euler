#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void ptPrint(int M[], int len);

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
	int *M;
	int i;
	int lower = (int)(sqrt(limit)) + 1;

	for (i = 0; i < limit; i++) {*(M + i) = 1;}

	for (i = 2; i < lower; i++) {
		mark(M, limit, i);
	}

	*M = limit - 1;
	*(M + 1) = 0;
	return (M);
	free(M);
}

void ptPrint(int *M, int len) {
	int i;
	for (i = 0; i < len; i++) {
		printf("%d: %d\n", i, *(M + i));
	}
}
