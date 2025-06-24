from heapq import heapify, heappushpop,heappop, heappush
class KthLargest:

    def __init__(self, k: int, nums):
        self.heap = [i for i in nums]
        self.k = k
        self.size = len(nums)
        heapify(self.heap)

        while(len(self.heap)>k):
            heappop(self.heap)
            self.size -=1


    def add(self, val: int) -> int:
        if(self.size < self.k):
            heappush(self.heap, val)
            self.size +=1
        elif(self.heap[0] < val):
            heappushpop(self.heap,val)
        return self.heap[0]
        
# s = KthLargest(3,[4,5,8,2])

# for i in [3,5,10,9,4]:
#     print(s.add(i))
# [null,4,5,5,8,8]


# s = KthLargest(4,[7,7,7,7,8,3])

# for i in [2,10,9,9]:
#     print(s.add(i))

# [null,7,7,7,8]

s = KthLargest(1,[])

for i in [-3,-2,-4,0,4]:
    print(s.add(i))

# [[2,[0]],[-1],[1],[-2],[-4],[3]]


# s = KthLargest(2,[0])

# for i in [-1,1,-2,-4,3]:
#     print(s.add(i))


# [null,-1,0,0,0,1]