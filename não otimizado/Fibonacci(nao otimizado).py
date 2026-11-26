import time
import tracemalloc

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

for n in range(0, 10):
    f = open("fib_log_not_optim_" + str(n) + "_.txt", "w", encoding="utf-8")
    for x in range(1, 46):
        tracemalloc.start()
        start = time.perf_counter()
        fib(x)
        end = time.perf_counter()
        f.write("n: " + str(x) + " | time elapsed: [" + str(end - start) + "] | memory used: [" + str(tracemalloc.get_traced_memory()) + "]")
        f.write("\n")
        #print("n: " + str(x) + " | time elapsed: [" + str(end - start) + "] | memory used: [" + str(tracemalloc.get_traced_memory()) + "]")
        tracemalloc.stop()
    f.close()