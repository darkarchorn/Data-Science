### Multithreading with thread pool executor

from concurrent.futures import ProcessPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"


if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_number, numbers)

    for result in results:
        print(result)