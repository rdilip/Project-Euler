#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void arrPrint(int M[], int len);

void mark(int sieve[], int len, int x) {
	int i;
	for (i = x + x; i < len; i += x) {
		sieve[i] = 0;
	}
}

int *primeSieve(int limit) {
	int M[limit];
	int i;
	int lower = (int)(sqrt(limit));

	for (i = 0; i < limit; i++) {M[i] = 1;}

	for (i = 2; i < lower; i++) {
		mark(M, limit, i);
	}


	int *T = M;	

	return (T);
}

void arrPrint(int M[], int len) {
	int i;
	for (i = 0; i < len; i++) {
		printf("%d: %d\n", i, M[i]);
	}
}
	
int main(int argc, char *argv[]) {
	int limit = atoi(argv[1]);
	int *R, i;
	R = primeSieve(limit);

	for (int i = 2; i < limit; i++) {
		if (*(R + i)) {
			printf("%d is prime\n", i);
		}
	}

	return 0;
}




