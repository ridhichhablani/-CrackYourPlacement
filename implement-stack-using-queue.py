class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        # Move all elements except the last one from queue1 to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # Pop the last element from queue1
        result = self.queue1.popleft()
        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def top(self) -> int:
        # Move all elements except the last one from queue1 to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # Get the last element from queue1
        result = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def empty(self) -> bool:
        return len(self.queue1) == 0

