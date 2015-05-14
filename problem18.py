import os
os.chdir("/Users/Rohit/Documents/Code/project_euler")
def text_input(file_name):
	M = []
	with open(file_name) as pyramid:
		for line in pyramid:
			M.append([int(i) for i in line.split()])
	return M

# maxpath(M) returns the maximum path recursively, M must be a pyramid
# double array
def maxpath(M):
	if len(M) == 1:return M[0][0]
	temp = M[len(M) - 2]
	for i in xrange(0,len(temp)):
		temp[i] = temp[i] + max(M[len(M) - 1][i],M[len(M) - 1][i + 1])
	M[len(M) - 2] = temp
	M.pop()
	return maxpath(M)
import time
start = time.time()
for i in xrange(0,5000):result =  maxpath(text_input("PEproblem18.txt"))
end = time.time()
print "The result is %d, and it took %f seconds to find that (5000 iterations)." % (result, end - start)

