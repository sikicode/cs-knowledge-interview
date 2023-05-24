# resource: https://www.geeksforgeeks.org/stack-in-python/
# stack properties: LIFO all functions O(1)
# use python list
stack = []
stack.append("a")
stack.append("b")
stack.append("c")

print(stack.pop())
print(stack.pop())

print(stack)

# use deque
# Python program to
# demonstrate stack implementation
# using collections.deque
from collections import deque
stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

# use queue to implement:
from queue import LifoQueue
q = LifoQueue(maxsize=3)
q.put(1)
q.get()
