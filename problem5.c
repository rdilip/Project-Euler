#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

long gcd(long a, long b) {
	long temp;
	while (b != 0) {
		temp = a;
		a = b;
		b = temp % b;
	}
	return a;
}


long lcm(long a, long b) {
	return (a * b) / (gcd(a, b));
}

long lcmm(long *numList, int len) {
	int i = 0;

	for (i = 0; i < len - 1; i++) {
		*(numList + i + 1) = lcm(*(numList + i), *(numList + i + 1));
	}

	return *(numList + len - 1);
}


int main(int argc, char *argv[]) {
	clock_t start, end;	
	start = clock();

	long nums[20];
	int i;
	for (i = 1; i <= 20; i++) {
		nums[i - 1] = i;
	}
	long *numList = nums;
	printf("The answer to problem5 is %lu\n", lcmm(numList, 20));
	end = clock();
	printf("The answer took %f seconds to find\n", (float)(end - start) / CLOCKS_PER_SEC);
}
	
