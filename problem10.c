#include <stdio.h>
#include <stdlib.h>
#include <math.h>


void mark(long *sieve, long len, long x) {
	long i;
	for (i = x + x; i < len; i += x) {
		*(sieve + i) = 0;
	}
}

/** Creates the sieve, non inclusive
 * First value is the number of elements represented 
 */

long *primeSieve(long limit) {
	long *M = calloc(limit, sizeof(long));
	long i, count;
	long lower = (long)(sqrt(limit)) + 1;
	for (i = 0; i < limit; i++) {
		M[i] = 1;
	}

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

int main(int argc, char *argv[]) {

	const char *lim = argv[1];
	char *e;
	long limit = strtol(lim, &e, 0);

	long *primes = primeSieve(limit);
	long long sum = 0;
	long i;

	for (i = 0; i < limit; i++) {
		if (*(primes + i)) {
			sum += i;
		}
	}

	printf("The answer to problem 10 is %lld\n", sum);
	return 0;
}
