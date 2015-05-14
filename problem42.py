# coding: utf-8
def l2n(inp):
    return sum([ord(c) - 64 for c in inp])
def triWd(inp):
    temp = l2n(inp)
    n = (-1.0 + ((1 + 8 * temp) ** 0.5)) / 2.0
    if n % 1 == 0:
        return True
    return False
def main():
    wds = []
    with open('p042_words.txt') as words:
        for line in words:            
            wds.extend(line.replace('"','').split(','))
    count = 0
    for i in wds:
        if triWd(i):
            count += 1
    return count
