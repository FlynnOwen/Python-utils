import time
from threading import Thread


def print_and_sleep(number):
    for i in range(number):
        time.sleep(1)
        print(i)


# Note that args argument must be used for parallelism
thread_1 = Thread(target=print_and_sleep, args=(10,))
thread_2 = Thread(target=print_and_sleep, args=(10,))

# Without using join, both threads will run asynchronously
start = time.time()
thread_1.start()
thread_2.start()
end = time.time()

# Takes 10 seconds
print(end - start)
