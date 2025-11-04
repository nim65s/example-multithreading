#!/usr/bin/env python

from time import perf_counter
from concurrent.futures import ThreadPoolExecutor

import httpx


def http_task():
    r = httpx.get("https://postman-echo.com/delay/1")
    return r.status_code


def pool(count: int) -> float:
    # ref. https://docs.python.org/3/library/concurrent.futures.html

    start = perf_counter()
    with ThreadPoolExecutor() as executor:
        for _ in range(count):
            executor.submit(http_task)
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    count = 100
    total = pool(count)
    print("total:", total)
    print("mean:", total / count)
