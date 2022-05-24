import time

'''seconds = 0
for i in range(10):    
    print('\r' + str(seconds), end='', flush=True)
    seconds = seconds + 1
    time.sleep(1)
'''
def timer(n, end):
    print('\r' + str(n), end='', flush=True)
    n = n + 1
    time.sleep(1)
    if n <= end:
        timer(n, end)

timer(0, 3)