import numpy as np
import random

arr = [random.randint(1,10) for _ in range(10)]
print(arr)

print(np.mean(arr))
print(np.var(arr))

arr2 = [(i - np.mean(arr))/np.std(arr) for i in arr]
print(arr2)

print(np.mean(arr2))
print(np.var(arr2))
