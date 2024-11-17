import time
import queue
import threading
import random

counter = 1
more_to_come = True


class Producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        global counter
        global more_to_come

        for i in range(5):
            time.sleep(random.randrange(2, 5))

            item = "news iteam #" + str(i)

            self.queue.put(item)
            counter += 1
            print("produced item: ", item)
        more_to_come = False


class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while more_to_come:
            item = self.queue.get(timeout=10)
            time.sleep(random.random())
            print(threading.current_thread().name, " popped :", item)
        print(threading.current_thread().name, " exiting")


q = queue.Queue()

prod = Producer(q)
cons = Consumer(q)

prod.start()
cons.start()


prod.join()
cons.join()
