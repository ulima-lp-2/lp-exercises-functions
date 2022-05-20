import time

seconds = 0
for i in range(10):    
    print('\r' + str(seconds), end='', flush=True)
    seconds = seconds + 1
    time.sleep(1)