import heapq

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]) or len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        return (self.large[0] + (-1 * self.small[0])) / 2

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())  # Output: 1.5
obj.addNum(3)
print(obj.findMedian())  # Output: 2