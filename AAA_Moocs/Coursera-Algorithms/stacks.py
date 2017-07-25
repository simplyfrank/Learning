"""
ABstract data type with the following operations:

- Push(key): add key to collection
- Key Top(key): returns the topmost key
- Key Pop(key): removes and returns the most recently-added key
- Boolean Empty(): checks if stack is empty
"""

class Stack(object):
    def __init__(self):
        pass


# Application (Balanced Parantheses)
def isBalanced(string):
    stack = Stack()
    for char in str:
        if char in ['(','[']:
            stack.Push(char)
        else:
            if stack.Empty():
                return False
            top = stack.Pop()
            if (top == "[" and char != "]") or (top == '(' and char != ')'):
                return False
        return stack.Empty()
