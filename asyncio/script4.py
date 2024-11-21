import asyncio
import time


async def greetings(message):
    for i in range(6):
        print(message)

        await asyncio.sleep(1)


async def print_numbers(numbers):
    for i in range(numbers):
        print(i)

        await asyncio.sleep(1)


async def main():
    start = time.time()
    await asyncio.gather(greetings("Hello"), greetings("world"), print_numbers(6))
    end = time.time()

    print("Total time: ", end - start)


asyncio.run(main())
