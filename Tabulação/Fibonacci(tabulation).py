import time
import tracemalloc


memo = {}
def fib(n):
    memo[0] = 0
    memo[1] = 1
    for i in range (2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

for n in range(0, 10):
    f = open("fib_log_table_opti_" + str(n) + "_.txt", "w", encoding="utf-8")
    for x in range(1, 46):
        memo.clear()
        tracemalloc.start()
        start = time.perf_counter()
        fib(x)
        end = time.perf_counter()
        f.write("n: " + str(x) + " | time elapsed: [" + str(end - start) + "] | memory used: [" + str(tracemalloc.get_traced_memory()) + "]")
        f.write("\n")
        tracemalloc.stop()
    f.close()