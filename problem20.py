def digitSum(num):
	num_list = list(str(num))
	num_list = [int(i) for i in num_list]
	return sum(num_list)
def factorial(num):
	if num == 0:return 1
	else:return num * factorial(num - 1)
print digitSum(factorial(100))
