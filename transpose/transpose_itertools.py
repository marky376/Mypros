#!/usr/bin/env python3
from itertools import chain
import time
import numpy as np

def transpose2(M):
    n = len(M[0])
    l = list(chain(*M))
    return [l[i::n] for i in range(n)]


matrix = np.array([[1,2,3], [4,5,6]]).tolist()

start = time.time_ns()

transposed = transpose2(matrix)

end = time.time_ns()

print(transposed)
print("Time taken", end-start, "ns")
