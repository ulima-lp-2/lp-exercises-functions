# write code
import random

def getRandom():
    r = random.randint(1,9)
    #print(r)
    return r

print('i\tend\tn\tsum\treduce')
def reduce(i, end, sum):
    n = getRandom()
    func = 'reduce'
    if i == end:
        func = sum
    print(i, '\t', end, '\t', n, '\t', sum, '\t', func)
    if i < end:
        sum_ = sum + n
        #print('sum:', sum_)
        return reduce(i + 1, end, sum_)
    else:
        return sum

print('suma: %d' % reduce(0, 5, 0))