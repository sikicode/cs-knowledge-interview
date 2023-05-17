# resource: https://www.geeksforgeeks.org/queue-in-python/
# FIFO O(1)

# list
q = []
q.append(1)
q.pop(0)

# deque:
from collections import deque
q = deque()
q.append(1)
q.popleft()

# queue
from queue import Queue
q = Queue(maxsize=3)
q.put(1)
q.get()