import asyncio
import time


async def greetings(message):
    for i in range(6):
        print(message)

        await asyncio.sleep(1)


async def main():
    start = time.time()
    task1 = asyncio.create_task(greetings("Hello"))
    task2 = asyncio.create_task(greetings("World"))

    await task1
    await task2

    end = time.time()

    print("Total time: ", end - start)


asyncio.run(main())
