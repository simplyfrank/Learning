"""
Queue is a Data Structure capable of storing items in a sorted order based on their collection.
It always returns the first-in item.
"""


class Queue(object):
    """
    Implements a simple Queue Object using a List.
    Follows FIFO Rules
    """

    def __init__(self, items=[]):
        self.items = items
    
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
