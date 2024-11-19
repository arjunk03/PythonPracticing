import multiprocessing
import time


def is_even(numbers, q):
    for n in numbers:
        if n % 2 == 0:
            q.put(n)
    # print(q)


def print_numbers(q):
    time.sleep(0.1)
    while not q.empty():
        time.sleep(0.01)
        print(q.get())


q = multiprocessing.Queue()

p1 = multiprocessing.Process(target=is_even, args=(range(10), q))
p2 = multiprocessing.Process(target=print_numbers, args=(q,))

p1.start()
p2.start()

p1.join()
p2.join()


def sender(connection, greets):
    for greet in greets:
        connection.send(greet)
    connection.close()


def recipient(connection):
    while True:
        greet = connection.recv()
        if greet == "STOP":
            break

        print(greet)


msgs = ["Hello", "world", "hi", "STOP"]
send_pipe, receiv_pipe = multiprocessing.Pipe()

p1 = multiprocessing.Process(target=sender, args=(send_pipe, msgs))
p2 = multiprocessing.Process(target=recipient, args=(receiv_pipe,))

p1.start()
p2.start()

p1.join()
p2.join()
