import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def print_and_sleep(number):
    for i in range(number):
        time.sleep(1)
        print(i)

    return number


# We are able to use a context manager with a thread-pool
with ThreadPoolExecutor(max_workers=2) as pool:
    futures = []
    for _ in range(2):
        # Ensuring to add the argument next to the function, rather than print_and_sleep(10)
        futures.append(pool.submit(print_and_sleep, 10))

    for future in as_completed(futures):
        print(future.result)
