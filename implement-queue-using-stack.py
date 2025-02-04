


class Stack:
    """
    An implementation of a stack following LIFO (Last in first out) order.

    === Attributes ===
    items: list - the items in a stack, where the front of the list is the bottom of the
                  stack
    """
    items: list

    def __init__(self) -> None:
        """
        Initiate a empty stack
        """
        self.items = []

    def pop(self) -> Any:
        """
        remove the top element of the stack and return it
        """
        return self.items.pop()

    def push(self, x: Any) -> None:
        """
        Push the item onto the top of the stack
        """
        self.items.append(x)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]


class MyQueue:
    """
    An implementation of queue using 2 stacks.

    === Attributes ===
    stack1: Stack - This stack will represent the queue. Top of the stack represents
    the front of the queue. Bottom of the stack represents the back of the queue.
    stack2: Stack - This stack will be used to manipulate the order inside of the queue
    """
    stack1: Stack
    stack2: Stack

    def __init__(self) -> None:
        """
        Initiate 2 empty stacks
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        """
        Enqueues the item to the bottom of the stack.
        """
        while not self.stack1.is_empty():
            item = self.stack1.pop()
            self.stack2.push(item)
        self.stack1.push(x)
        while not self.stack2.is_empty():
            item = self.stack2.pop()
            self.stack1.push(item)
            
    def pop(self) -> int:
        """
        Dequeues the first item from the top of the stack
        """
        return self.stack1.pop()

    def peek(self) -> int:
        """
        returns the item at the front of the list, however do not remove it
        from the queue
        """
        item = self.stack1.pop()
        self.stack1.push(item)
        return item
    
    def empty(self) -> bool:
        return self.stack1.is_empty()
