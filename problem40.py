def main():
    s = ''
    for i in xrange(0,400000):
        s += str(i)
    d = list(s)
    n = reduce(lambda x, y:x*y, [int(d[10**i]) for i in xrange(0,7)])
    return n
