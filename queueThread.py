import concurrent.futures
import time
from queue import Queue


def worker(task_id):
    print(f"Task {task_id} started")
    time.sleep(2)  # Simulate work
    print(f"Task {task_id} completed")


# Create a bounded queue with a max size
max_queue_size = 2  # Limit the number of queued tasks
task_queue = Queue(maxsize=max_queue_size)


class BoundedThreadPoolExecutor(concurrent.futures.ThreadPoolExecutor):
    def submit(self, *args, **kwargs):
        if task_queue.full():
            raise RuntimeError("Task queue is full! Cannot submit more tasks.")
        task_queue.put(None)  # Simulate adding a task to the queue
        return super().submit(*args, **kwargs)


pool = BoundedThreadPoolExecutor(max_workers=2)

try:
    # Submit more tasks than the queue allows
    pool.submit(worker, 1)
    pool.submit(worker, 2)
    pool.submit(worker, 3)  # This will raise an error
except RuntimeError as e:
    print(f"Error: {e}")

pool.shutdown(wait=True)
print("Main thread continuing to run")
