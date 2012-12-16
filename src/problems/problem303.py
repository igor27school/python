'''
Created on Dec 15, 2012

@author: Igor
'''

import heapq

HIGHEST_ALLOWED = 2

# Check if all the digits are in the right range
def sat_const(n):
    for chr in str(n):
        if int(chr) > HIGHEST_ALLOWED:
            return False
    return True

# Pre-loading values that are hard to find
f_dict = {9:1358,
          99:11335578,
          999:111333555778,
          9999:1111333355557778}

# Finding the right multiplier starting from the last digit
# keeping the list of endings that produce products with good endings
def f(n):
    if sat_const(n):
        return 1
    if n in f_dict:
        return f_dict[n]
    if n % 10 == 0:
        print "Processing %d" % n
        return f(n/10)
    DIGITS = range(10);
    numbers_to_try = range(1, 10)
    good_mults = []
    mod = 10
    while True:
        heapq.heapify(numbers_to_try)
        while len(numbers_to_try) > 0:
            number = heapq.heappop(numbers_to_try)
            product_tail = (n * number) % mod
            if sat_const(product_tail):
                good_mults.append(number)
                if sat_const(number * n):
                    f_dict[n] = number
                    return number
        numbers_to_try = [mod * digit + number for digit in DIGITS for number in good_mults]
        mod *= 10

def run():
    MAX = 10000
    sum = 0
    for i in xrange(1, MAX+1):
        sum += f(i)
    print "The sum is %d" % sum

if __name__ == '__main__':
    import time
    start_time = time.time()
    run()
    print time.time() - start_time, "seconds"
