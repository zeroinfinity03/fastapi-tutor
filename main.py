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
    print("Total time taken:", total_time, "s")
    
    return {
        "message": "All tasks completed!",
        "start_time": start,
        "end_time": timer() - total_time + start,
        "total_time": str(round(total_time, 2)) + " s"
    }