import redis
import time

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

while True:
    # Block and pop a task from the queue
    task = r.brpop(["MAIN_TUBE"])

    if task:
        print(f"Processing task: {task}")
    else:
        print("No tasks in the queue. Waiting...")
        time.sleep(1)
