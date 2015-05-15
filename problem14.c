/* Author: Rohit Dilip
 * Date: 2015/05/15
 * ----------------------
 * PROBLEM 14
 * Given the Collatz sequence as follows:
 * if n is even, n = n / 2
 * if n is odd, n = 3n + 1
 * We can generate chains of numbers that eventually end at 1. 
 * What starting number under one million produces the largest chain?
 * To solve this problem, we use a technique called memoization. We
 * store the chain lengths as we execute the sequence, and thus can
 * later access already found chain lengths if we re encounter them.
 */		

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#define LIMIT 1000000

/* funtion: collatz
 * ------------------
 * Given an input number, begins to perform the Collatz sequence. First 
 * searches for the number in the cache, if found, adds that value's 
 * chain length to the current chain length. If not found, executes
 * collatz sequence on the number until a known chain length is found
 * or the number reaches one, increments count by one each time.

 * 
 * val: value of input number
 * chain: length of current chain
 * 
 */

unsigned collatz(unsigned long n, unsigned int *cachePtr) {
	unsigned count = 1;
	//printf("The starting value is %lu\n", n);
	while (n > 1) {
		if (n < LIMIT && cachePtr[n] != 0) {
			//printf("\tFound in memory\n");
			count += cachePtr[n] - 1;
			break;
		} else if (n % 2 == 0) {
			//printf("\t%lu Is even --> %lu\n", n, n / 2);
			n /= 2;
		} else {
			//printf("\t%lu is odd --> %lu\n", n, 3 * n + 1);
			n = 3 * n + 1;
		}
		count ++;
	}
	//printf("\tThe final count is %d\n", count);


	return count;
}

/* funtion: find_max_collatz
 * ------------------
 * Given a mimum input value, a maximum input value, and a pointer
 * to the number cache, this executes the collatz sequence on every
 * value between min and max, finding the largest chain by continually
 * comparing the chain length of iter (between min and max) with the
 * max chain length (m).

 * min: minimum value in range
 * max: maxmum value in range
 * cachePtr: Pointer to cache array
 * m: largest chain length
 * num: number corresponding to largest chain length
 * count: current working chain length
 * iter: current working number
 * 
 * returns: The number yielding the largest chain length between min and max
 */

unsigned long find_max_collatz(unsigned int min, unsigned int max, unsigned int *cachePtr) {
	unsigned int m = 1;
	unsigned long num = 1;
	unsigned int count = 1;
	unsigned long iter = min;
	
	//unsigned int M[LIMIT];

	while (iter < max) {
		count = collatz(iter, cachePtr);
		if (count > m) {
			m = count;
			num = iter;
		}

		if (iter < LIMIT) {
			cachePtr[iter] = count;
		}

		iter += 1;
	}


	return num;
}

int main(int argc, char *argv[]) {
	clock_t start, end;
	start = clock();
	int i;
	unsigned long ans;
	unsigned int CACHE[LIMIT];	

	for (i = 0; i < LIMIT; i++) {
		CACHE[i] = 0;
	}

	unsigned int *cachePtr = CACHE;

	ans = find_max_collatz(1, LIMIT, cachePtr);
	end = clock();
	printf("The answer is %lu, and it took %f seconds to find\n", ans, 				(float)(end - start) / CLOCKS_PER_SEC);
}
