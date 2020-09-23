""""
program of two functions
"""

import time

stat_time = time.perf_counter()

def do_something(senconds):
    print(f'Slepping {senconds} seconds...')
    time.sleep(senconds)
    print(f'Done Sleeping...{senconds}')

do_something(1)
do_something(1)

end_time = time.perf_counter()

print(f'Finished in {round(end_time-stat_time, 2)} seconds')