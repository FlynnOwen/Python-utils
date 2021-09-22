import time
from threading import Thread


def print_and_sleep(number):
    for i in range(number):
        time.sleep(1)
        print(i)


# Note that args argument must be used for parallelism
thread_1 = Thread(target=print_and_sleep, args=(10,))
thread_2 = Thread(target=print_and_sleep, args=(10,))

# By using join, we force one thread to finish before another starts
start = time.time()

thread_1.start()
thread_1.join()

thread_2.start()
thread_2.join()

end = time.time()

# Takes 20 seconds
print(end - start)
