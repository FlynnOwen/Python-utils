import time
from threading import Thread, Lock

x = 0


# using a lock ensures that the global variable can be shared across threads
def test_function(lock):
    global x

    with lock:
        local_x = x

        # process
        local_x += 1
        time.sleep(0.5)
        x = local_x


lock = Lock()
thread_1 = Thread(target=test_function, args=(lock,))
thread_2 = Thread(target=test_function, args=(lock,))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(x)