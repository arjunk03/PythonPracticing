import time
import queue

q = queue.PriorityQueue()

q.put(5)
q.put(4)
q.put(1)
q.put(2)
q.put(3)


while not q.empty():
    print(q.get())
