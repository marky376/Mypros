#!/usr/bin/env python3
# gen2.py

async def main():
    # This does *not* introduce concurrent execution
    # It is meant to show syntax only

    g = [i async for i in mygen()]
    f = [j async for j in mygen()if not (j // 3 % 5)]
    return g, f

# The entire management of the event loop has been implicitly handled by one function call
g, f = asyncio.run(main())

