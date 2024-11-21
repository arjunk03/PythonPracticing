import asyncio
import time


async def greetings(message):
    for i in range(6):
        print(message)

        await asyncio.sleep(1)


start = time.time()
asyncio.run(greetings("Hello"))
asyncio.run(greetings("World"))

end = time.time()

print("Total time: ", end - start)


async def greetings(message):
    for i in range(6):
        print(message)

        await asyncio.sleep(1)


async def main():
    start = time.time()
    await greetings("Hello")
    await greetings("World")

    end = time.time()

    print("Total time: ", end - start)


asyncio.run(main())
