
import time

def func1():
    for _ in range(100000):
        print("*")

def func2():
    for _ in range(100000):
        print("#")

start_time = time.perf_counter()
func1()
func2()
end_time = time.perf_counter()
print("time total : ",end_time-start_time)
