#include <stdio.h>
#include <stdlib.h>

int problem1(int limit) {
	int i = 0;
	int sum = 0;
	for (i = 0; i < limit; i++) {
		if (i % 3 == 0 || i % 5 == 0) {
			sum += i;
		}
	}

	return sum;
}

int main(int argc, char *argv[]) {
	int limit = atoi(argv[1]);
	printf("The answer to Problem 1 is %d\n", problem1(limit));
}
