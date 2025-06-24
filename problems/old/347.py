import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        for k2, v in counter.items():
            heapq.heappush(heap, (-v, k2))

        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop(heap)[1])
        return ans


s = Solution()

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))


# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

print(s.topKFrequent([1], 1))
