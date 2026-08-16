from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.stream = []

        
        

    def next(self, val: int) -> float:
        self.stream.append(val)
        div = 0
        avg=0
        if len(self.stream) >= self.size:
            div = self.size
        else:
            div = len(self.stream)
        avg = sum(self.stream[-self.size: ])/div

        return avg



        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)