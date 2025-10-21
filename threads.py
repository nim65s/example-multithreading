#!/usr/bin/env python

from time import perf_counter
from concurrent.futures import ThreadPoolExecutor

from task import task


def pool(count: int) -> float:
    # ref. https://docs.python.org/3/library/concurrent.futures.html

    start = perf_counter()
    with ThreadPoolExecutor() as executor:
        for _ in range(count):
            executor.submit(task)
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    count = 4
    total = pool(count)
    print("total:", total)
    print("mean:", total / count)
