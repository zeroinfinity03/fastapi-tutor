
import asyncio
from timeit import default_timer as timer


async def run_task(name, seconds):
    print(name, "started at:", timer())
    await asyncio.sleep(seconds)
    print(name, "completed at:", timer())


async def main():
    start = timer()
    await asyncio.gather(
        run_task('Task 1', 2),
        run_task('Task 2', 1),
        run_task('Task 3', 3)
    )
    print("Total time taken:", timer() - start, "s")


asyncio.run(main())



# Time 1000.0:
# ├─ Task 1 started (2 sec sleep)
# ├─ Task 2 started (1 sec sleep)
# └─ Task 3 started (3 sec sleep)

# Time 1001.0:
# └─ Task 2 completed (fastest)

# Time 1002.0:
# └─ Task 1 completed

# Time 1003.0:
# └─ Task 3 completed (slowest)

# Total: 3 seconds (max sleep time) ← 3 seconds! (2x faster)





# API examples: 

'''

import asyncio
from fastapi import FastAPI
from timeit import default_timer as timer

app = FastAPI()


@app.get("/wait")
async def wait():
    start = timer()
    await asyncio.sleep(3)  # Non-blocking sleep
    end = timer()
    duration = end - start
    
    return {
        "message": "Finished waiting!",
        "start_time": start,
        "end_time": end,
        "duration_seconds": duration
    }


# User 1 (Browser 1): Opens http://127.0.0.1:8000/wait (Time: 0 sec)
# User 2 (Browser 2): Opens http://127.0.0.1:8000/wait (Time: 0 sec, same time!)
# User 3 (Browser 3): Opens http://127.0.0.1:8000/wait (Time: 0 sec, same time!)


#####################################################################################################


import asyncio
from fastapi import FastAPI
from timeit import default_timer as timer

app = FastAPI()


async def run_task(name, seconds):
    print(name, "started at:", timer())
    await asyncio.sleep(seconds)
    print(name, "completed at:", timer())


@app.get("/tasks")
async def main():
    start = timer()
    await asyncio.gather(
        run_task('Task 1', 2),
        run_task('Task 2', 1),
        run_task('Task 3', 3)
    )
    total_time = timer() - start
    print(f"Total time taken: {total_time:.2f} s")
    
    return {
        "message": "All tasks completed!",
        "total_time": f"{total_time:.2f} s"
    }



'''