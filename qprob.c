#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include <time.h>

/**
 * This program is designed to simulate and solve the following problem. Given three
 * random values, a, b, and c, all of which are bounded by [1, n], what is the probability
 * that two of the values sum to the third?
 */

void ptrPrint(int *nums, int len) {
	int i = 0;
	for (i = 0; i < len; i++) {
		printf("%d\n", *(nums + i));
	}
}

int *randNum(int num, int max) {
	int *randnums = calloc(num, sizeof(int));
	int i;
	int r = rand();

	for (i = 0; i < num; i++) {
		r = rand();
		*(randnums + i) = (int)((r / (double)RAND_MAX) * max) + 1;
	}

	return(randnums);
	
}

int cond(int a, int b, int c) {
	if (a + b == c) {
		return 1;
	} else if (a + c == b) {
		return 1;
	} else if (b + c == a) {
		return 1;
	} 

	return 0;
}

int main(int argc, char *argv[]) {
	int n = atoi(argv[1]);
	char *temp = argv[2];
	char *e;
	long sim = strtol(temp, &e, 0);

	int success = 0;
	long i = 0;
	int *randnums = calloc(3, sizeof(int));

	srand(time(NULL));

	for (i = 0; i < sim; i++) {
		randnums = randNum(3, n);
		if (cond(*randnums, *(randnums + 1), *(randnums + 2))) {
			
			success++;
		} 
	}

	free(randnums);

	printf("Success: %d\nSimulations:  %ld\n", success, sim);
	printf("Probability of success: %f\n", (double)success / sim);

	return 0;
}

