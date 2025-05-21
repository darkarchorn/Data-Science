### Multithreading
## When to use Multithreading
### I/O-bound task: Task that spend more time waiting for I/O operations (e.g., file operations,...)
### Concurrent execution: When you want to improve the throughput of your application by performing multiple application concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")

def print_letter():
    for letter in "ABCDE":
        time.sleep(1)
        print(f"Letter: {letter}")

# Create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t= time.time()

## Start the threads
t1.start()
t2.start()

## Wait for the threads to complete
t1.join()
t2.join()
finished_time = time.time() - t
print(finished_time)

# Finish time is reduce in half