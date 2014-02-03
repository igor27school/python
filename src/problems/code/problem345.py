import math

sums = {}

def solve(ifile, ofile):
    lines = ifile.readlines()
    matrix = [[int(n) for n in line.strip().split()] for line in lines] 
    max_sum = find_max_sum(matrix)
    ofile.write(str(max_sum))

def find_max_sum(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    key = get_key(matrix)
    if key in sums:
        return sums[key]
    ret = 0
    for i in xrange(size):
        new_matrix = [line[1:] for line in matrix
            if matrix.index(line) != i]
        s = matrix[i][0] + find_max_sum(new_matrix)
        if s > ret:
            ret = s
    sums[key] = ret
    return ret
       
def get_key(matrix):
    return str(matrix)
