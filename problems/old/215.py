import heapq
from collections import deque
# class Solution:
#     def findKthLargest(self, nums, k: int) -> int:
#         heapq._heapify_max(nums)
#         for _ in range(k-1):
#             heapq._heappop_max(nums)
#         return nums[0]


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = []
        
        size = len(nums)
        for i in range(size):
            heapq.heappush(heap, nums[i])
            if(i > k -1):
                heapq.heappop(heap)
        return heap[0]













s = Solution()

print(s.findKthLargest([3,2,1,5,6,4],2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6],4))
        