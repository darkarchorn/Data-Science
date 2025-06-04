'''
Real -World Example: Multiprocessing for CPU- bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers,
involve significant computation work. Multiprocessing
can be used to distribute the workload across multiple
CPU cores, improving performance.
'''

import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## Function to compute factorial of a given number

def factorial(number):
    print(f"Computine the factorial of {number}...")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [i for i in range(5000, 6000)]
    start_time = time.time()

    ## create a pool of worker processes

    with ProcessPoolExecutor(max_workers=61) as ppe:
        results = ppe.map(factorial, numbers)
    end_time  = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")