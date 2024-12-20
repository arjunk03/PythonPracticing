import concurrent.futures

import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)

    time.sleep(2)

    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as t:
        t.map(thread_function, range(3))


# if "test":
