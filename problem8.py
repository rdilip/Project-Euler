import os
strnum = ""
numlist = []
path = "/users/rohit/documents/code/project_euler"
os.chdir(path)
with open("problem8.txt") as num:
	for line in num:
		strnum += (line.rstrip("\n"))
		numlist = list(strnum)
		numlist = [int(i) for i in numlist]
val = 0
for i in xrange(0,len(numlist)-14):
	prod = reduce(lambda x, y: x*y, numlist[i:i+13])
	if prod > val:
		val = prod
print val
print numlist[len(numlist)-13:len(numlist)]
