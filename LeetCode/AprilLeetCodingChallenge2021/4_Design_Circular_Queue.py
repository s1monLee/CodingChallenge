class MyCircularQueue:
    myQueue = [None]*1000
    maxSize = 0
    trueSize = 0
    start = 0
    end = 0
    def __init__(self, k: int):
        self.maxSize = k

    def enQueue(self, value: int) -> bool:
        if (self.end - self.start) < self.maxSize:
            self.myQueue[self.end] = value
            self.end += 1
            self.trueSize+=1
            return True
        return False

    def deQueue(self) -> bool:
        if self.start != self.end:
            self.myQueue[self.start] = None
            self.start += 1
            self.trueSize-=1
            return True
        return False

    def Front(self) -> int:
        if self.trueSize == 0:
            return -1
        return self.myQueue[self.start]

    def Rear(self) -> int:
        if self.trueSize == 0:
            return -1
        return self.myQueue[self.end-1]

    def isEmpty(self) -> bool:
        return self.trueSize == 0

    def isFull(self) -> bool:
        return self.trueSize == self.maxSize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
