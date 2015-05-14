#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void ptrPrint (long *M, long len) {
	long i;
	for (i = 0; i < len; i++) {
		printf("%ld: %ld\n", i, *(M + i));
	}
}

long *primeSieve(long numPrimes) {
	long primes[numPrimes];
	long primeCand = 0;
	int state;

	// i runs along primes until we hit a limit
	// j runs down the primes already discovered in primes

	int i, j;
	long sqrtCheck;
	// Intializing the array to 0
	for (i = 0; i < numPrimes; i++) {primes[i] = 0;}
	primes[0] = 2; // First prime is 2;

	i = 1;
	j = 0;

	while (i < numPrimes) {
		sqrtCheck = (long)sqrt(numPrimes) + 1;

		for (j = 0; primes[j] < sqrtCheck; j++) {
			if (primeCand % primes[j] == 0) {
				state = 0;
				break;
			} 
		}

		if (state) {
			primes[i] = primeCand;
			i++;
		}
		primeCand += 2;
		state = 1;
	}
	printf("Testing\n");
	long *primeList = primes;	

	return(primeList);
}

int main(int argc, char *argv[]) {
	const char *temp = argv[1];
	char *e;
	unsigned long limit = strtol(temp, &e, 0);
	printf("Limit is %lu\n", limit);
	long *ans = primeSieve(limit);
	printf("testing\n");
	ptrPrint (ans, limit);

	return 0;
}



