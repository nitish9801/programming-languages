import time
import asyncio
import aiohttp


async def worker(name, n, session):
    print(f'worker-{name}')
    url = f'https://qrng.anu.edu.au/API/jsonI.php?length={n}&type=uint16'
    response = await session.request(method='GET', url=url)
    return response.text()

async def main():
    async with aiohttp

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f'executed in {elapsed:0.2f} seconds')