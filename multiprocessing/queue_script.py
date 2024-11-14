import queue

q = queue.Queue()
print(q.queue)
print(q.empty())

for i in range(7):
    q.put(i)

print(q.queue)
print(q.empty())

while not q.empty():
    print(q.get())
print(q.queue)
print(q.empty())
