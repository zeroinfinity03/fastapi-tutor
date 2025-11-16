
import time
from timeit import default_timer as timer


def run_task(name, seconds):
    print(name, "started at:", timer())
    time.sleep(seconds)
    print(name, "completed at:", timer())


start = timer()
run_task('Task 1', 2)
run_task('Task 2', 1)
run_task('Task 3', 3)
print("Total time taken:", timer() - start, "s")



# Task 1 started at: 1000.0
# Task 1 completed at: 1002.0
# Task 2 started at: 1002.0
# Task 2 completed at: 1003.0
# Task 3 started at: 1003.0
# Task 3 completed at: 1006.0
# Total time taken: 6.00 s  ← 6 seconds!