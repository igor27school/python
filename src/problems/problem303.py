'''
Created on Dec 15, 2012

@author: Igor
'''

MAX = 10000
undiscovered_numbers = range(1, MAX+1)
undiscovered_numbers.remove(9999)
dict = {9999:1111333355557778}

# The less numbers we have left, the less we iterate
def crossout_numbers(number):
    # Can't remove numbers while iterating, remember them
    list_remove = []
    for n in undiscovered_numbers:
        if number % n == 0:
            list_remove.append(n)
            dict[n] = number / n
    # Remove numbers from the list because we found their value
    for n in list_remove:
        # Also use f(10*n) = f(n)
        counter = n
        while counter in undiscovered_numbers:
            undiscovered_numbers.remove(counter)
            dict[counter] = dict[n]
            counter *= 10

def to_base(n, base):
    answer = 0
    mult = 1
    while (n > 0):
        answer += mult * (n % base)
        n //= base
        mult *= 10
    return answer

def fill_dict():
    BASE = 3
    i=1
    while undiscovered_numbers and i < 3**16:
        n = to_base(i, BASE)
        crossout_numbers(n)
        i += 1

def run():
    fill_dict()
    answer = sum(dict.values())
    print "The sum is %d" % answer

if __name__ == '__main__':
    import time
    start_time = time.time()
    run()
    print time.time() - start_time, "seconds"
