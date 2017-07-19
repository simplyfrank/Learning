"""
So linked lists, it's named kind of like links in a chain, right, so we've got a head pointer that points to a node that then has some data and points to another node, 
points to another node and eventually points to one that doesn't point any farther.

Contains:
- Key (the value for the node)
- next pointer (the pointer pointing to the next value node)

Operations:
- PushFront(key) : Add to Front of the list
- Key topFront() : return front Item from list
- PopFront() : remove front item
- PushBack(Key) : add to back
- Key TopBack() : return back item
- PopBack() : remove back item
- Boolean Find(Key) : find if key in list
- Erase(Key) : remove key from list
- Boolean Empty() : empty list?
- AddbBefore(Node, Key) : Add value before a given node
- AddAfter(Node, Key) : Add value after given node


Based on Coursera at https://www.coursera.org/learn/data-structures/lecture/kHhgK/singly-linked-lists
"""
import numpy as np

class Node(object):
    """
    The representational ground unit for our linkedList.
    It stores a value(key) and a pointer to the next element in the list
    """
    def __init__(self, key, next=None):
        self.key = key
        self.next = next



class LinkedList(object):

    def __init__(self, values):
        # append all values to the list
        self.linkedList = np.array()
        # Keeps track of the beginning of the list
        self.headPointer = None
        # Keeps track of the ending of the list
        self.tailPointer = None

    
    def setHead(self, node):
        """
        Convenience Function to set the value of the headPointer
        """
        assert isinstance(node, Node)
        if not self.headPointer:
            self.headPointer = self.tailPointer = node
        else:
            self.headPointer = node
        return None

    def setTail(self, node):
        """
        Convenience Function to set the value of the headPointer
        """
        assert isinstance(node, Node)
        if not self.tailPointer:
            self.setHead(node)
        self.setTail(node)
        return None


    def getLength(self):
        """
        Returns the length of the linkedList
        """
        assert self.linkedList
        return len(self.linkedList)

    def pushFront(self, key, inplace=False):
        """
        Order 1 operation
        """
        # Create a new node with the key as its value and link it to the current head
        assert isinstance(key, int)
        node = Node(key, next=self.headPointer)
        # update the headPointer to now point to the new node
        self.setHead(node)
        # if inplace==True: return None else return linkedList
        return None if not inplace else self.linkedList
        


    def popFront(self):
        """
        Find the first element in the list remove it from the list and return it.
        """
        assert self.headPointer
        # Update the headpointer to point to the first elements next
        first_element = self.headPointer
        self.setHead(self.headPointer.next)
        # remove the first element from the list
        remove(first_element)

        if not self.headPointer:
            self.tailPointer = None
        # return the first element
        return first_element



    def pushBack(self, key, inplace=False):
        """
        Requires a tail pointer to work nicely. Otherwise we need to traverse the whole List to find and and add the new key
        """
        # Allocate a new node
        node = Node(key, next=self.tailPointer)
        # Update the current last element to point to new node
        self.tailPointer.next = node
        # Update tailPointer to point to new Element
        self.setTail(node)
        # if inplace==True: return None else return linkedList
        return self.linkedList if inplace else None

    def popBack(self):
        """
        Find the last element in the list remove it from the list and return it to the main scope
        """
        assert self.headPointer
        if self.headPointer == self.tailPointer:
            self.headPointer = self.tailPointer = None
        else:
            p = self.headPointer
            while p.next.next:
                p = p.next
            p.next = None
            self.setTail(p)

        # Identify the element next to the last element

        # Remove the last element

        # Update tailPointer to point to next to last element

        # Return removed element

    def addAfter(self,node, key):
        node2 = Node(key)
        node2.next = node.next
        node.next = node2
        if self.tailPointer == node:
            self.setTail(node2)

    