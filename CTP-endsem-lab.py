import time
import tracemalloc

n = int(input("Enter number of transactions: "))

transactions = [
    int(input(f"Transaction {i + 1}: ₹"))
    for i in range(n)
]

threshold = int(input("Enter threshold value: ₹"))


def measure_list():
    tracemalloc.start()

    start = time.perf_counter()

    result = [x for x in transactions if x > threshold]

    time_taken = time.perf_counter() - start

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, time_taken, peak / 1024


def measure_generator():
    tracemalloc.start()

    start = time.perf_counter()

    result = (x for x in transactions if x > threshold)
    count = sum(1 for _ in result)

    time_taken = time.perf_counter() - start

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return count, time_taken, peak / 1024


lst, lt, lm = measure_list()
gen_count, gt, gm = measure_generator()


print("\nList-based Processing")
print("Records processed:", len(lst))
print("Execution time:", round(lt, 6), "seconds")
print("Peak memory:", round(lm, 2), "KB")

print("\nGenerator-based Processing")
print("Records processed:", gen_count)
print("Execution time:", round(gt, 6), "seconds")
print("Peak memory:", round(gm, 2), "KB")