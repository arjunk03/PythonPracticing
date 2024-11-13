import random
import time
import threading

cond = threading.Condition()

container = []
counter = 1
more_to_come = True


def produce():
    global container
    global counter
    global more_to_come

    for i in range(5):
        time.sleep(random.randrange(2, 5))
        cond.acquire()

        item = "News item #" + str(counter)

        container.append(item)
        counter += 1

        print("produced : ", item)
        cond.notify_all()

        cond.release()
    more_to_come = False
