from threading import Thread
from time import sleep, time


def func(thread_index):
    """
    This function sleeps for 1.5 seconds
    """
    print('start', thread_index)
    sleep(1.5)
    print('stop', thread_index)


# single thread
start = time()
[func(i) for i in range(10)]
print("no thread runtime:", (time() - start))

# threading
start = time()

threads = [Thread(target=func, args=[i]) for i in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print("thread runtime:", (time() - start))