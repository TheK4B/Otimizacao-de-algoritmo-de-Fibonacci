import time
import tracemalloc


memo = {}
def fib(n):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

for n in range(0, 10):
    f = open("fib_log_memo_opti_" + str(n) + "_.txt", "w", encoding="utf-8")
    for x in range(1, 46):
        memo.clear()
        tracemalloc.start()
        start = time.perf_counter()
        fib(x)
        end = time.perf_counter()
        f.write("n: " + str(x) + " | time elapsed: [" + str(end - start) + "] | memory used: [" + str(tracemalloc.get_traced_memory()) + "]")
        f.write("\n")
        #print("n: " + str(x) + " | time elapsed: [" + str(end - start) + "] | memory used: [" + str(tracemalloc.get_traced_memory()) + "]")
        tracemalloc.stop()
    f.close()