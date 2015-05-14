def triples(m, n):
	k = 1
	while True:
		yield 2 * k * m * (m + n)
		k += 1

def sides(m, n):
	res = []
	k = 1
	while 2 * k * m * (m + n) <= 1000:
		res.append([k*(m*m - n*n), 2*m*n*k, k*(m*m + n*n)])
		k += 1
	return res


P = [[0]] * 1001 # 1001 spaces so that I can refer to P[i] with i as the actual number. P[1000] is perimeter of 1000, etc. Obviously P[0] is going to be 0, no problems there.

for i in xrange(3, 24):
	for j in xrange(1, i):
		for k in sides(i, j):
			try:
				P[sum(k)].append(k)
			except IndexError:
				continue

M = [set(k) for R in P for k in R]
