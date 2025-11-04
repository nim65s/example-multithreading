#!/usr/bin/env python

import asyncio
from time import perf_counter

import httpx


async def http_task(client):
    r = await client.get("https://postman-echo.com/delay/1")
    return r.status_code


async def pool(count: int) -> float:
    # ref. https://docs.python.org/3/library/concurrent.futures.html

    start = perf_counter()
    async with httpx.AsyncClient() as client:
        tasks = [http_task(client) for _ in range(count)]
        await asyncio.gather(*tasks)
    end = perf_counter()

    return end - start


if __name__ == "__main__":
    count = 100
    total = asyncio.run(pool(count))
    print("total:", total)
    print("mean:", total / count)
