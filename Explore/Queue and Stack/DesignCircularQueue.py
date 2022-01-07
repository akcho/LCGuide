class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.filled_slots = 0  # how many slots in q are actually being used
        self.fixed_size = k  # fixed queue size (set by k)

    def setTail(self):
        return ((self.head + self.filled_slots) % self.fixed_size) - 1

    def enQueue(self, value: int) -> bool:
        if self.filled_slots == self.fixed_size:
            return False
        self.filled_slots += 1
        tail = self.setTail()
        self.queue[tail] = value
        return True

    def deQueue(self) -> bool:
        if self.filled_slots == 0:
            return False
        self.head = (self.head + 1) % self.fixed_size
        self.filled_slots -= 1
        return True

    def Front(self) -> int:
        if self.filled_slots == 0:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.filled_slots == 0:
            return -1
        tail = self.setTail()
        return self.queue[tail]

    def isEmpty(self) -> bool:
        return self.filled_slots == 0

    def isFull(self) -> bool:
        return self.filled_slots == self.fixed_size

    