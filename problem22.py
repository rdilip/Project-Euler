import os
import time
from numba import jit
starttime = time.time()
os.chdir("/Users/rohit/Documents/code/project_euler")
@jit
def a2n(x):
	return ord(x) - 64
@jit
def numSum(name):
	sumList = [a2n(i) for i in list(name)]
	return sum(sumList)
M = []
with open("PEproblem22.txt") as text:
	for line in text:M.extend(line.split(","))
M = [i[1:-1] for i in M]
M = sorted(M)
numM = [numSum(i)*(M.index(i) + 1) for i in M]
print sum(numM)
endtime = time.time()
print endtime - starttime
