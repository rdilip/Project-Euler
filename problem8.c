#include <stdio.h>
#include <stdlib.h> 
#include <math.h>

void ptrPrint (int *M, int len) {
	int i;
	for (i = 0; i < len; i++) {
		printf("%d: %d\n", i, *(M + i));
	}
}

long mulInt(int *nums, int start, int end) {
	int i = 0;
	long prod = 1;
	int temp;

	for (i = start; i < end; i++) {
		temp = *(nums + i);

		if (temp == 0) {
			return 0;
		}

		prod *= (long)*(nums + i);
	}

	return prod;
}

// this makes all my pointer values ones
void makeOnes(int *nums, int len) {
	int i = 0;

	for (i = 0; i < len; i++) {
		*(nums + i) = 1;
	}
}

int *getNum(const char *filename) {

	int *nums = malloc(sizeof(int));


	FILE *fr = fopen(filename, "rt"); 
	int i = 0;
	int largest_num = 0;
	int nextChar = getc(fr);

	while (nextChar != EOF) {
		*(nums + i) = (int)(nextChar) - '0';	
		nextChar = getc(fr);
		if (nextChar == '\n') {nextChar = getc(fr);}
		i++;
	}

	return(nums);
}

int main(int argc, char *argv[]) {

	int *nums = getNum("problem8.txt");
	int len = 13;
	long largest_num = 0;	
	long temp;
	int i;

	for (i = 0; i < 1000 - len; i++) {
		temp = mulInt(nums, i, i + len);		
		if (temp > largest_num) {
			largest_num = temp;
		}
	}
	
	printf("The answer to problem 8 is %lu\n", largest_num);

	return 0;
}
				

