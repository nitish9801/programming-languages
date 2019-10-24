import time
from random import randint
import asyncio


def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd

async def square_odds(start, stop):
    for odd in odds(start, stop):
        await asyncio.sleep(2)
        yield odd ** 2

async def randn():
    await asyncio.sleep(2)
    return randint(1, 10)


async def main():
    # r = await randn()
    # print("r:", r)

    start = time.perf_counter()
    # n = await randn()
    r = await asyncio.gather(*(randn() for _ in range(100)))
    elapsed_time = time.perf_counter() - start
    print('{}, time elapsed {}'.format(r, elapsed_time))

    async for odd in square_odds(11, 17):
        print(odd)



if __name__=="__main__":
    asyncio.run(main())