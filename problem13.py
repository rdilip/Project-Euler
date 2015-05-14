import os
os.chdir("/Users/rohit/Documents/Code/project_euler")
M = []
with open("PEproblem13_INT.txt") as text:
	for line in text:
		M.append(long(line.rstrip("\n")))
print str(sum(M))[0:11]
