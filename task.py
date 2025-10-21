#! /usr/bin/env python
from time import perf_counter

import numpy as np


def task(size=6000) -> float:
    """
    chronomètre le temps de résolution d’un système Ax=b de taille `size`.

    on s’attend à ce que la résolution d’un problème de taille 6000 prenne 2 à 3 secondes:

    >>> 2 < task(size=6000) < 3
    True
    """
    A = np.random.rand(size, size)
    b = np.random.rand(size)

    start = perf_counter()
    np.linalg.solve(A, b)
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    print(task())
