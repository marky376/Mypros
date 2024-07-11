import asyncio

async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print("World!")


routine = main()
asyncio.run(routine)
