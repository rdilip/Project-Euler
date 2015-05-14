import time
numbers = ["zero one two three four five six seven eight nine".split()]
irregular = "ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
numbers.append("twenty thirty forty fifty sixty seventy eighty ninety".split())
power = "hundred thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion".split()
def num2letter(num):#works for all numbers less than 1000
	diglen = len(str(num))		
	if diglen == 1: 
		return numbers[0][num] #base case
	elif diglen == 2 and num - (num % 10) == 10: 
		return irregular[(num % 10)]#accounting for 11-19 "irregulars"
	elif diglen == 2 and num % 10 == 0:
		return numbers[1][((num - (num % 10)) / 10) - 2]
	elif diglen == 2:
		return numbers[1][((num - (num % 10))/10) - 2] + " " + numbers[0][num % 10]
	elif diglen == 3 and num % 100 == 0:
		dig = (num - (num % 10**(diglen - 1))) / (10**(diglen - 1))
		num = num % (10**(diglen - 1))
		return numbers[0][dig] + " " + power[diglen-3]
#Recursively stripping the leading number and calling the function again	
	elif diglen == 3:
		dig = (num - (num % 10**(diglen - 1))) / (10**(diglen - 1))
		num = num % (10**(diglen - 1))
		return (numbers[0][dig] + " " + power[diglen-3] + " and " + num2letter(num))

def num2letterX(num):#works for all numbers...I hope
	'''
For this method, in accordance with general English language, I strip away the number in partitions of three. For example, the number 12,345,678, I initially only look at 12, then 345, then 678. I simply use the original num2letter program to convert those chunks, and add on the appropriate power of 10^3 (thousand, million, billion...). 
	'''
	diglen = len(str(num))
	diglentemp = int((diglen-1) / 3) * 3 #This is used to find what power of 10^3 to add on
	temp = (num - num % (10**(diglentemp))) / (10**(diglentemp)) #This takes only the numbers in the first partition
	if diglen > 3 and (num % 10**int(((diglen-1)/3)*3) == 0):#for the case of a number divisible by the next partition -- example, 342000 / 1000 = 0
		num = num % (10**(diglentemp)) #This reduces the number to the next partition
		return num2letter(temp) + " " + power[int(diglen / 3)]
	elif diglen > 3: 
		num = num % (10**(diglentemp)) #This reduces the number to the next partition
		return num2letter(temp) + " " + power[int(diglen / 3)] + " " + num2letterX(num)
	else:#Since the other method has the base case, this refers all digits less than three to that method
		return num2letter(num)
def PEproblem17(limit):
	tot = 0
	for i in xrange(1,limit+1):
		tot += len(num2letterX(i).replace(' ',''))
	return tot
start = time.time()
result = PEproblem17(1000)
end = time.time()
print "The answer is %d , and that took %f seconds." % (result, end-start)
