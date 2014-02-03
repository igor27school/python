'''
Created on Dec 15, 2012

@author: Igor
'''

BASE = 3
# For the given n, find the smallest tri-base representation
# for every remainer mod n
def f(n):
    if(n < BASE):
        return 1
    dic = {}
    for i in xrange(1, BASE):
        dic[i] = i
    known_remainders = list(reversed(range(1, BASE)))
    while known_remainders:
        x = known_remainders.pop()
        x *= 10
        for j in xrange(BASE):
            if (x+j) % n == 0:
                return (x+j) / n
            elif (x+j) % n not in dic:
                dic[(x+j) % n] = x+j
                known_remainders.insert(0, x+j)
    raise Exception


def run():
    MAX = 10000
    sum = 0
    for i in xrange(1, MAX+1):
        number = f(i)
        sum += number
    print "The sum is %d" % sum

if __name__ == '__main__':
    import time
    start_time = time.time()
    run()
    print time.time() - start_time, "seconds"

