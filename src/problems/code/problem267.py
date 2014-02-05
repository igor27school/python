import math

def solve():
    GOAL = math.pow(10, 9)
    times = 1000
    do = lambda x: give_number(x, GOAL, times)
    low = 0.14
    inc = 0.001
    n = low
    for i in xrange(20):
        count, number = do(n)
        print "Numbers: %f, %d, %f" % (n, count, number)
        n += inc
        
def give_number(f, goal, iterations):
    good_factor = 1 + 2 * f
    bad_factor = 1 - f
    counter_good = 0
    counter_bad = 0
    number = 1
    while number < goal:
        number *= good_factor
        counter_good += 1
    while counter_good + counter_bad < iterations:
        if number * bad_factor >= goal:
            number *= bad_factor
            counter_bad += 1
        else:
            number *= good_factor
            counter_good += 1
    return tuple([counter_good, number])

def find():
    n = 1000
    p = 432
    row = get_pascal(n)
    lower_sum = sum(row[:p])
    total = math.pow(2, n)
    print "Sums: %d, %d" % (lower_sum, total)
    ten_to_twelve = math.pow(10, 12)
    prob_not = int(ten_to_twelve * lower_sum / total)
    answer = ten_to_twelve - prob_not
    print "The answer is 0.%d" % answer


def get_pascal(n):
    row = [1]
    for i in xrange(n):
        new_row = [1]
        for j in xrange(1, len(row)):
            new_row.append(row[j-1] + row[j])
        new_row.append(1)
        row = new_row
    return row

if __name__ == "__main__":
    find()
