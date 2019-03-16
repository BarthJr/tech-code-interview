# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# get_min() -- Retrieve the minimum element in the stack.


"""
>>> minStack = MinStack()
>>> minStack.push(2147483646)
>>> minStack.push(2147483646)
>>> minStack.push(2147483647)
>>> minStack.top()
2147483647
>>> minStack.pop()
>>> minStack.get_min()
2147483646
>>> minStack.pop()
>>> minStack.get_min()
2147483646
>>> minStack.pop()
>>> minStack.push(2147483647)
>>> minStack.top()
2147483647
>>> minStack.get_min()
2147483647
>>> minStack.push(-2147483648)
>>> minStack.top()
-2147483648
>>> minStack.get_min()
-2147483648
>>> minStack.pop()
>>> minStack.get_min()
2147483647
"""
import math


class MinStack:
    def __init__(self):
        self.queue = []
        self.min_value = [math.inf]

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.min_value.append(min(self.min_value[-1], x))

    def pop(self) -> None:
        if self.queue:
            self.queue.pop()
            self.min_value.pop()

    def top(self) -> int:
        if self.queue:
            return self.queue[-1]

    def get_min(self) -> int:
        return self.min_value[-1]
