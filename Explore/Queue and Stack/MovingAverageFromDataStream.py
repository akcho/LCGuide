# Circular Queue
# time: O(1)
# space: O(n)
class MovingAverage:
    def __init__(self, size: int):
        self.q = [0] * size
        self.window_size = size
        self.head = 0
        self.window_sum = 0
        self.total = 0  # number of elements seen so far

    def next(self, val: int) -> float:
        self.total += 1
        self.head = (self.head + 1) % self.window_size
        self.window_sum = self.window_sum - self.q[self.head] + val
        self.q[self.head] = val
        return self.window_sum / min(self.window_size, self.total)