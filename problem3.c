#include <stdio.h>
#include <stdlib.h>
#include <math.h>

unsigned long problem3(unsigned long limit) {
	// Removing factors of two
	unsigned long largest_factor = 1;
	unsigned long i;
	unsigned long temp = limit;

	while (temp % 2 == 0) {
		largest_factor = 2;
		temp = temp / 2;
	}
	
	i = 3;
	while (temp != 1) {
		while (temp % i == 0) {
			largest_factor = i;
			temp = temp / i;
		}
		i += 2;
	}
	
	return (largest_factor);
}

int main(int argc, char *argv[]) {
	const char *temp = argv[1];
	char *e;
	unsigned long limit = strtol(temp, &e, 0);
	printf("The limit is %lu\n", limit);
	printf("The answer to problem 3 is %lu\n", problem3(limit));
}
	
