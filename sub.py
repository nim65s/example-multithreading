#!/usr/bin/env python

from time import perf_counter

from subprocess import Popen


def sub(count: int) -> float:
    # ref. https://docs.python.org/3/library/subprocess.html

    start = perf_counter()

    processes = [Popen(["./task.py"]) for _ in range(count)]
    for p in processes:
        p.wait()
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    count = 4
    total = sub(count)
    print("total:", total)
    print("mean:", total / count)
