import os
os.chdir("/users/rohit/documents/code/project_euler")
M = []
with open("PEproblem11_INT.txt") as num:
	for line in num:
		numtemp = [int(x) for x in line.rstrip("\n").split()]
		M.append(numtemp)
max_prod = 0
for i in xrange(0,17):
	for j in xrange(0,20):
		#up down products
		prod = M[i][j] * M[i+1][j] * M[i+2][j] * M[i+3][j]
		if max_prod < prod:max_prod = prod
		#left right products
		prod = M[j][i] * M[j][i+1] * M[j][i+2] * M[j][i+3]
		if max_prod < prod:max_prod = prod

for i in xrange(0,17):
	for j in xrange(0,17):
		#diagonal
		prod = M[i][j] * M[i+1][j+1] * M[i+2][j+2] * M[i+3][j+3]
		if max_prod < prod:max_prod = prod
for i in xrange(3,20):
	for j in xrange(0,17):
		prod = M[i][j] * M[i-1][j+1] * M[i-2][j+2] * M[i-3][j+3]
		if max_prod < prod:max_prod = prod
print max_prod
