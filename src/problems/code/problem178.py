h = {}
TOP_DIGIT = 9

def solve():
    DIGIT_LIMIT = 40
    answer = 0
    for i in xrange(1, TOP_DIGIT):
        answer += go(0, DIGIT_LIMIT-1, i)
    answer += go(2, DIGIT_LIMIT-1, TOP_DIGIT)
    print "The answer is %d" % answer

def go(goals, left, last):
    # What is left to hit, how many left, last number
    # 0 = neither 0 nor 9 was reached
    # 1 = 0 was reached, not 9
    # 2 = 9 was reached, not 0
    # 3 = both were reached
    if left == 0 and goals != 3:
        return 0
    if left == 0 and goals == 3:
        return 1
    if goals == 0 and left <= TOP_DIGIT:
        return 0
    if goals == 1 and left < TOP_DIGIT - last:
        return 0
    if goals == 1 and left == TOP_DIGIT - last:
        return 1
    if goals == 2 and left < last:
        return 0
    if goals == 2 and left == last:
        return 1
    key = tuple([goals, left, last])
    if key in h:
        return h[key]
    # Not in the hash yet, put it there
    if last == 0:
        ret = go(goals, left-1, 1)
    elif last == TOP_DIGIT:
        ret = go(goals, left-1, TOP_DIGIT-1)
    elif last == 1 and goals % 2 == 0:
        ret = go(goals+1, left-1, 0) + go(goals, left-1, 2)
    elif last == TOP_DIGIT-1 and goals < 2:
        ret = go(goals+2, left-1, TOP_DIGIT) \
            + go(goals, left-1, TOP_DIGIT-2)
    else:
        ret = go(goals, left-1, last-1) + go(goals, left-1, last+1)
    # Count itself as a solution
    if goals == 3:
        ret += 1;
    h[key] = ret
    return ret

if __name__ == "__main__":
    solve()
