#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct chainVal {
	long val;
	int chain;
} chainVal;

int search(chainVal *vals, long itm , long len);

int collatz (chainVal *vals, int len, long start, int chain) {
	int temp = search(vals, start, len);
	if (start == 1) {
		return chain;
	} else if (temp) {
		return (temp);
	} else if (start % 2 == 0) {
		return (vals, len, collatz(start / 2, chain + 1));
	} else {
		return (vals, len, collatz(3 * start + 1, chain + 1));
	}
}



int search(chainVal *vals, long itm , long len) {
	long i;

	for (i = 0; i < len; i++) {
		if (vals->val == itm) {
			return (vals->chain);
		}
	}

	return 0;
}

long problem14 (long limit) {
	long i;
	long count = 0;
	long max_chain = 0;
	long max_num = 0;

	for (i = 0; i < limit; i++) {
				

int main(int argc, char *argv[]) {
	int test = atoi(argv[1]);
	printf("%d\n", collatz((long)test, 1));
}
		
