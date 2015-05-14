#include <stdio.h>
#include <stdlib.h>

#define MAX_FIB 4000000

int problem2() {
	
	int sum = 0;
	int a, b, c;

	a = 1;
	b = 2;

	while (b < MAX_FIB) {
		c = a;
		a = b;
		b = c + a;

		if (b % 2 == 0) {sum += b;}
	}

	return sum;
}

int main(int argc, char *argv[]) {
	printf("The answer to problem 2 is %d\n", problem2());
}

	
