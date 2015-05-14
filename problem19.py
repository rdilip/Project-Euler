# coding: utf-8
D = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
D2 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def day():
    count = 1
    while True:
        yield count
        count += 1
        if count > 7: count = 1
dweek = day()
day =0 
count = 0
year = 0
while year < 100:
    if year % 4 == 0 or year == 100:
        for i in D2:
            temp = D2[i]
            for d in xrange(1, temp + 1):
                day = dweek.next()
                if day == 7 and d == 1:
                    count += 1
    else:                  
        for i in D:
            temp = D[i]
            for d in xrange(1, temp + 1):
                day = dweek.next()
                if day == 7 and d == 1:
                    count += 1
    year += 1
print count
