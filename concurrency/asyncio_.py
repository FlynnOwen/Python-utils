import asyncio
import time


async def print_number(number):
    await asyncio.sleep(2)
    print(number)


async def main_default(numbers: tuple):
    start = time.time()
    for number in numbers:
        await print_number(number)
    end = time.time()

    print('sync took ' + str(end - start) + 'seconds')


async def main_async(numbers: tuple):
    start = time.time()
    await asyncio.gather(*[print_number(i) for i in numbers])
    end = time.time()
    
    print('sync took ' + str(end - start) + 'seconds')


if __name__ == '__main__':
    asyncio.run(main_default((1, 2, 3, 5)))

    asyncio.run(main_async((1, 2, 3, 5)))
