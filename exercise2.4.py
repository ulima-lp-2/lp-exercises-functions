# write code
import random

def getRandom():
    r = random.randint(1,9)
    # print(r)
    return r

print('i\tend\tnumero\tsum_\tfunc')
def sum(i, end, sum_):
    numero = getRandom()
    func = sum_
    if i < end:
        func = 'sum'
    print(i, '\t', end, '\t', numero, '\t', sum_, '\t', func)
    sum_ = sum_ + numero
    if i < end:
        return sum(i + 1, end, sum_)
    else:
        return sum_

s = sum(0, 5, 0)
print(s)