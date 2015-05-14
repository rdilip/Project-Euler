#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MIN_PROD_VAL 100
#define MAX_PROD_VAL 1000

int isPali(int n) {
	int n1 = n;
	int n2 = 0;
	int temp = 0;

	while (n1 >= 1) {
		n2 *= 10;
		temp = n1 % 10; 
		n1 = (n1 - (n1 % 10)) / 10;
		n2 += temp;
	}

	if (n2 == n) {return 1;}
	else return 0;
}

int main(int argc, char *argv[]) {
	int i, j;
	int largest_pali = 1;

	for (i = MIN_PROD_VAL; i < MAX_PROD_VAL; i++) {
		for (j = i; j < MAX_PROD_VAL; j++) {
			if (isPali(i * j) && (i * j) > largest_pali) {
				largest_pali = i * j;
			}
		}
	}

	printf("The answer to problem 4 is %d\n", largest_pali);
}
	
