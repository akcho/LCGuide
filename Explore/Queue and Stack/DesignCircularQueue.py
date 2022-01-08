# time: O(1)
# space: O(n)

from threading import Lock


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.capacity = k
        self.head = 0
        self.filled_slots = 0
        self.q_lock = Lock()

    def getTail(self):
        return ((self.head + self.filled_slots) % self.capacity) - 1

    def enQueue(self, value: int) -> bool:
        with self.q_lock:
            if self.isFull(): return False
            self.filled_slots += 1
            self.q[self.getTail()] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % self.capacity
        self.filled_slots -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.getTail()]

    def isEmpty(self) -> bool:
        return self.filled_slots == 0

    def isFull(self) -> bool:
        return self.filled_slots == self.capacity

