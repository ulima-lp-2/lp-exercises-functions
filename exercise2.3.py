import time

seconds = 0
for i in range(10):    
    print('\r' + str(seconds), end='', flush=True)
    seconds = seconds + 1
    time.sleep(1)

def timer(seconds, end):
    if seconds < end:
        print('\r' + str(seconds), end='', flush=True)
        time.sleep(1)
        return timer(seconds + 1, end)

timer(0, 10)