import time
from threading import Thread

x = 0


def test_function():
    global x

    local_x = x

    # process
    local_x += 1
    time.sleep(0.5)
    x = local_x


thread_1 = Thread(target=test_function)
thread_2 = Thread(target=test_function)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(x)