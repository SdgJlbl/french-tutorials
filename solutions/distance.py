import math
def distance(a, b):
    d = 0
    for i, j in zip(a, b):
        d += math.fabs(i - j)
    return d
