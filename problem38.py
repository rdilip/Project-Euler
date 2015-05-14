# coding: utf-8
def isPan(num):
    temp = filter(lambda x: x != "0", list(num))
    if len(set(temp)) == 9:
        return True
    return False
