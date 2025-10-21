from time import perf_counter

import numpy as np


def task(size=6000):
    A = np.random.rand(size, size)
    b = np.random.rand(size)

    start = perf_counter()
    x = np.linalg.solve(A, b)
    end = perf_counter()

    print(end - start)


if __name__ == "__main__":
    task()
