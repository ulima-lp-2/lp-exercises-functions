# write code
import random

def getRandom():
    r = random.randint(1,9)
    #print(r)
    return r

print('i\tend\tn\tsum')
def reduce(i, end, sum):
    n = getRandom()
    print(i, '\t', end, '\t', n, '\t', sum)
    if i < end:
        sum_ = sum + n
        #print('sum:', sum_)
        return reduce(i + 1, end, sum_)
    else:
        return sum

print('suma: %d' % reduce(0, 5, 0))