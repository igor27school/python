import math

def solve():
    # The initial number is a*x + b, starts at 1*x + 0
    # State contains original a, original b, current a, current b
    state = [1, 0, 1, 0]
    for o in "UDDDUdddDDUDDddDdDddDDUDDdUUDd":
        state = update_state(state, o)
    print "Final state: %s" % state
    n = long(math.pow(10, 15))
    factor = n / state[0]
    answer = state[0] * factor + state[1]
    if answer <= n:
        answer += state[0]
    print "The answer is %d" % answer

def do_nothing(state):
    print "Curiously, we got here with state: %s" % state

def impossible(state):
    print "We are in an impossible state: %s" % state

# X = 3Y + 0
def plus_zero(state):
    return [state[0]*3, state[1], state[2]*3, state[3]]

# X = 3Y + 1
def plus_one(state):
    return [state[0]*3, state[1]+state[0], state[2]*3, state[3]+state[2]]

# X = 3Y + 2
def plus_two(state):
    return [state[0]*3, state[1]+2*state[0], state[2]*3,
        state[3]+2*state[2]] 

options = {"D00":do_nothing,
           "D01":impossible,
           "D02":impossible,
           "D10":plus_zero,
           "D11":plus_two,
           "D12":plus_one,
           "D20":plus_zero,
           "D21":plus_one,
           "D22":plus_two,
           "U00":impossible,
           "U01":do_nothing,
           "U02":impossible,
           "U10":plus_one,
           "U11":plus_zero,
           "U12":plus_two,
           "U20":plus_two,
           "U21":plus_zero,
           "U22":plus_one,
           "d00":impossible,
           "d01":impossible,
           "d02":do_nothing,
           "d10":plus_two,
           "d11":plus_one,
           "d12":plus_zero,
           "d20":plus_one,
           "d21":plus_two,
           "d22":plus_zero
           }

def downward(state):
    return [state[0], state[1], state[2]/3, state[3]/3]

def upward(state):
    return [state[0], state[1], state[2]*4/3, (state[3]*4+2)/3]

def small_downward(state):
    return [state[0], state[1], state[2]*2/3, (state[3]*2-1)/3]

operations = {"D":downward,
              "U":upward,
              "d":small_downward
             }
# State and operation
def update_state(state, o):
    a1 = state[2] % 3
    b1 = state[3] % 3
    state = options[o+str(a1)+str(b1)](state)
    state = operations[o](state)
    return state

if __name__ == "__main__":
    solve()
