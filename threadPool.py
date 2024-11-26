import concurrent.futures
import time

def worker(task_id):
    print(f"Task {task_id} started")
    time.sleep(2)  # Simulate work
    print(f"Task {task_id} completed")

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

# Submit 3 tasks
pool.submit(worker, 1)
pool.submit(worker, 2)
pool.submit(worker, 3)

pool.shutdown(wait=True)
print("Main thread continuing to run")
