# coding: utf-8
def isPan(num):
    temp = filter(lambda x: x!= '0', list(num))
    if len(set(temp)) == 9:
        return True
    return False
def main():
    p = set()
    for i in xrange(2,80):
        start = 1234 if i < 10 else 123
        for j in xrange(start, 10000 // i):
            if isPan(str(i) + str(j) + str(i*j)):
                p.add(i*j)
    return sum(p)
print main()
