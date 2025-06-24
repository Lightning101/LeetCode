from heapq import heappush, heappop, heapify
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap,-num)

        heappush(self.minHeap, -heappop(self.maxHeap))

        if(len(self.maxHeap)< len(self.minHeap)):
            heappush(self.maxHeap, - heappop(self.minHeap))


    def findMedian(self) -> float:
        if (len(self.maxHeap) > len(self.minHeap)):
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0] + -self.maxHeap[0])/2.0
        
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())
# obj.addNum(3)
# print(obj.findMedian())

# [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
obj.addNum(-1)
print(obj.findMedian())
obj.addNum(-2)
print(obj.findMedian())
obj.addNum(-3)
print(obj.findMedian())
obj.addNum(-4)
print(obj.findMedian())
obj.addNum(-5)
print(obj.findMedian())
# [null,null,-1.00000,null,-1.50000,null,-2.00000,null,-2.50000,null,-3.00000]