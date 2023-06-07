# resource: https://www.geeksforgeeks.org/heap-data-structure/
# time complexity: insert/delete O(lgN), lookup O(1), heapify O(N)
# heapify time: https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
from collections import heapq
heap = heapq.heapify([])
heapq.heappush(heap, 1)
heapq.heappop(heap)
