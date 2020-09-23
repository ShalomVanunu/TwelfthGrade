""""
program of two functions with Thread
"""

import time
import threading

stat_time = time.perf_counter()

def do_something(senconds):
    print(f'Slepping {senconds} seconds...')
    time.sleep(senconds)
    print(f'Done Sleeping...{senconds}')

t1 = threading.Thread(target=do_something, args=(1,))
t2 = threading.Thread(target=do_something, args=(1,))
t1.start() #startthe threading
t2.start()
t1.join() # wait until thread ends
t2.join()


end_time = time.perf_counter()

print(f'Finished in {round(end_time-stat_time, 2)} seconds')