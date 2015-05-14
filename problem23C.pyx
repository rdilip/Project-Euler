cdef check(int num):
	tot_sum = []
	for i in xrange(1,int(num**0.5) + 1):
		if num % i == 0:
			tot_sum.append(i)
			tot_sum.append(num / i)
	tot_sum.remove(num)
	temp = set(tot_sum)
	return sum(temp) > num
		
def problem23C(int limit):
	abundant = [i for i in xrange(1,limit) if check(i)]
	abnSum = [False] * limit #if false, then they cannot be written as sum of two abn numbers
	cdef int tot

	for i in xrange(len(abundant)):
		for j in xrange(i,len(abundant)):
			if abundant[i] + abundant[j] < limit:
				abnSum[abundant[i] + abundant[j]] = True
	tot = 0
	for i in xrange(0,limit):
		if not abnSum[i]:
			tot += i
	return tot
