#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include <time.h>

int main(int argc, char *argv[]) {
	char *test = argv[1];
	char *e;
	long max = strtol(test, &e, 0); 
	int i;
	unsigned int r;
	srand(time(NULL));	
	for (i = 0; i < max; i++) {
		r = rand();
		printf("%d\n", r);
	}
	return 0;
}
