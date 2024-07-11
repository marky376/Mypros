#!/usr/bin/env python3
# mygen.py

async def mygen(u: int = 10):

    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)
