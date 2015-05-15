/* PROBLEM 14
 * Given the Collatz sequence as follows:
 * if n is even, n = n / 2
 * if n is odd, n = 3n + 1
 * We can generate chains of numbers that eventually end at 1. 
 * 		What starting number under one million produces the largest chain?
 *		To solve this problem, we use a technique called memoization. 
 * 		Instead of trying to compute all the chain lengths, which would tak
 *		a very unsigned long long time, we store the lengths of the chains, aunsigned long long with
 * 		the starting value, and search for the value as we go aunsigned long long. 
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define LIMIT 10

typedef struct chainVal {
	unsigned long long val;
	unsigned long long chain;
} chainVal;

unsigned long long search(chainVal *vals, unsigned long long itm , unsigned long long len);

/* funtion: collatz
 * ------------------
 * Performs the collatz sequence on a given input value, and increments
 * the chain by one in the process.
 * 
 * val: value of input number
 * chain: length of current chain
 * 
 */

	
void collatz (unsigned long long *val, unsigned long long *chain) {
	unsigned long long temp_val = *val;
	unsigned long long temp_chain = *chain;

	if (temp_val % 2 == 0) {
		temp_val /= 2;
		temp_chain ++;
	} else {
		temp_val = temp_val * 3 + 1;
		temp_chain ++;
	}

	*val = temp_val;
	*chain = temp_chain;
}


/* function: search
 * ------------------
 * Searches for a specific chainVal within a memory
 *
 * itm: Specific value to search for
 * len: Length of memory
 * vals: Pointer to first chainVal in memory
 *
 * returns: the length of the chain if the value is there, otherwise 0
 */

unsigned long long search(chainVal *vals, unsigned long long itm , unsigned long long len) {
	unsigned long long i;

	for (i = 0; i < len; i++) {
		if (vals->val == itm) {
			return (vals->chain);
		}
	}

	return 0;
}

unsigned long long problem14 () {
	unsigned long long i; 
	unsigned long long val;
	unsigned long long *valPtr;

	unsigned long long len = 0;

	unsigned long long *chainLenPtr;
	unsigned long long chainLen;

	unsigned long long maxChainLen = 0;
	chainVal inp;

	chainVal *vals = malloc(sizeof(chainVal));

	for	(i = 1; i < LIMIT; i++) {
		chainLen = 0;
		chainLenPtr = &chainLen;
		
		val = i;
		//printf("Testing value %ld\n", val);
		valPtr = &val;

		while (val != 1) {
			collatz(valPtr, chainLenPtr);
			if (search(vals, val, len)) {
				chainLen += search(vals, val, len); 
				break;
			}
		}
		chainLen++;
		//printf("\tThis has %ld terms\n", chainLen);
		if (chainLen > maxChainLen) {
			maxChainLen = chainLen;
		}

		inp.val = i;
		inp.chain = chainLen;
		*(vals + i) = inp;
		len ++;
	}

	return(maxChainLen);
}

int main(int argc, char *argv[]) {
	printf("%llu\n", problem14());
}
		
