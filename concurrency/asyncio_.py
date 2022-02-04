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

# Event-loop can't sit in main thread
loop = asyncio.get_event_loop()

if __name__ == '__main__':
    numbers = (1, 2, 3, 5)
    asyncio.run(main_default(numbers))

    asyncio.run(main_async(numbers))

    # Using event-loop
    loop.run_until_complete(main_async(numbers))
