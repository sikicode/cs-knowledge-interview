# O(1) insertion, delete, and lookup
# https://wiki.python.org/moin/TimeComplexity
# design hashmap: https://leetcode.com/problems/design-hashmap/
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(0)

    def insert(self, newValue):
        # if not existed, add the new element to the head.
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            # set the new head.
            self.head.next = newNode

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False


# Support Concurrency:
# - Java: ConcurrentHashMap class - https://www.geeksforgeeks.org/concurrenthashmap-in-java/
# - Python:
#     - https://superfastpython.com/thread-safe-dictionary-in-python/
#     - https://stackoverflow.com/questions/6953351/thread-safety-in-pythons-dictionary
# Auto rehashing: https://www.geeksforgeeks.org/load-factor-and-rehashing/
# Handle Collision:
# - Use a prime number as bucket size: https://planetmath.org/goodhashtableprimes
# - Separate Chaining: https://www.geeksforgeeks.org/separate-chaining-collision-handling-technique-in-hashing/
# - Open Addressing (linear/quadratic probing and double hashing): https://www.geeksforgeeks.org/open-addressing-collision-handling-technique-in-hashing/
