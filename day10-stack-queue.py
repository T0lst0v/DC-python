# mplement a Stack data structure in Python.
# Create a class called "Stack" which consists of two methods push and pop.
# The push method will add a value to the stack and
# pop method will pop out the last value inserted into the stack.


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, i):
        if i is not None:
            self.arr.append(i)

    def pop(self):
        if len(self.arr) > 0:
            item = self.arr[-1]
            del self.arr[-1]
            return item
        else:
            return None


stack = Stack()

for i in range(20, 30):
    stack.push(i)

print(stack.pop())
print(stack.arr[0])


# Activity - Queue
# Implement a Queue data structure in Python.
# Create a class called "Queue" which consists of two methods "enqueue" and "dequeue".
# The enqueue method will add an element to the queue and the dequeue method will dequeue the element from the queue.
