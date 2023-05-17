class ListNode:
    def __init__(self, data, next = ListNode):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = ListNode(data)
        if (self.head):
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode

