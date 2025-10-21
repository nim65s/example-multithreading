#! /usr/bin/env python
from time import perf_counter

import numpy as np


def task(size=6000) -> float:
    A = np.random.rand(size, size)
    b = np.random.rand(size)

    start = perf_counter()
    np.linalg.solve(A, b)
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    print(task())
