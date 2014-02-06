import math

def solve():
    a = "%s%s" % ("14159265358979323846264338327950288419716939937510",
                  "58209749445923078164062862089986280348253421170679")
    b = "%s%s" % ("82148086513282306647093844609550582231725359408128",
                  "48111745028410270193852110555964462294895493038196")
    answer = ""
    for i in xrange(18):
        n = (127 + 19 * i) * long(math.pow(7, i))
        rem = n % 100
        whole = n / 100
        large, small = find_fibs(whole)
        if get_letter(large-whole, large, small) == 0:
            answer = a[rem-1] + answer
        else:
            answer = b[rem-1] + answer
    print "The answer is %s" % (answer)

def find_fibs(n):
    a = 1
    b = 1
    i = 1
    while b <= n:
        t = b
        b += a
        a = t
        i += 1
    return [b, a]

# the letter is n-th from the back of b
def get_letter(n, b, a):
    while b > 1:
        t = a
        a = b - a
        b = t
        if n > b:
            n -= b
            t = a
            a = b - a
            b = t
    return a


if __name__ == "__main__":
    solve()
