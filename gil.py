#!/usr/bin/env python

from time import perf_counter
from concurrent.futures import ThreadPoolExecutor


def cpu_task():
    s = 0
    for _ in range(100_000_000):
        s += 1
    return s


def pool(count: int) -> float:
    # ref. https://docs.python.org/3/library/concurrent.futures.html

    start = perf_counter()
    with ThreadPoolExecutor() as executor:
        for _ in range(count):
            executor.submit(cpu_task)
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    count = 4
    total = pool(count)
    print("total:", total)
    print("mean:", total / count)
