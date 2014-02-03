'''
Created on Dec 15, 2012

@author: Igor
'''

values = {}

# length_number is how many digit spots are left to fill
# limits is a tuple of (how many digits can be used once more,
# how many digits can be used up to two times, etc. up to MAX_DIGITS
def number_numbers(length_number, limits):
    if length_number == 0:
        return 1
    # Memoization
    key = "%d%s" % (length_number, limits)
    if key in values:
        return values[key]
    value = 0
    for i in xrange(len(limits)):
        # If there are no digits that can be used i+1 times, skip the call 
        if limits[i] == 0:
            continue
        # Modify the tuple to prepare for recursive call
        list_limits = list(limits)
        list_limits[i] -= 1
        if i > 0:
            list_limits[i-1] += 1
        new_limits = tuple(list_limits)
        # Using one of the digits in the ith position moves it into (i-1)st 
        # position and reduces the number of unfilled spots by 1
        value += limits[i] * number_numbers(length_number-1, new_limits)
    values[key] = value
    return value

def run():
    LENGTH_NUMBER = 18
    NUMBER_DIGITS = 10
    MAX_DIGITS = 3
    # At the beginning, any number except 0 can be used
    # After a digit (say 1) is in the first spot, there is one number that
    # can be used at most 2 times and there are 9 numbers that can be used
    # at most 3 times: (0, 1, 9)
    list_limits = [0] * MAX_DIGITS
    list_limits[MAX_DIGITS-1] = NUMBER_DIGITS - 1
    list_limits[MAX_DIGITS-2] = 1
    limits = tuple(list_limits)
    # Since the first digit can be anything but zero, the multiplier is 9
    answer = (NUMBER_DIGITS - 1) * number_numbers(LENGTH_NUMBER-1, limits)
    print "The answer is %d" % answer

if __name__ == '__main__':
    import time
    start_time = time.time()
    run()
    print time.time() - start_time, "seconds"
