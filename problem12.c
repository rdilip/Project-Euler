#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int numDivisors(long num) {
	int count = 0;
	long i = 1;

	for (i = 1; i < (long)sqrt(num) + 1; i++) {
		if (i == num % i) {
			count++;
		} else if (num % i == 0) {
			count += 2;
		}
	}

	return count;
}

int main(int argc, char *argv[]) {

	int max = atoi(argv[1]);
	clock_t start, end;
	start = clock();

	int divnum = 0;
	int i = 2;
	unsigned long long triangle = 1;

	do {
		triangle += i;
		i++;
		divnum = numDivisors(triangle);
	} while (divnum <= max);

	end = clock();

	printf("The answer to problem 12 is %lld\n", triangle);
	printf("The answer took %f seconds to get\n", (double)(end - start) / 
		CLOCKS_PER_SEC);
}
