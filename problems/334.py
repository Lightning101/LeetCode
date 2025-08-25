import heapq


class Solution:

    def todt(self, sol, heap):
        if len(sol) == 3:
            return True
        if not heap:
            return False

        node = heapq.heappop(heap)
        left = self.todt(sol[:], heap[:])
        right = False
        if not sol or (sol[-1][0] < node[0] and sol[-1][1] < node[1]):
            right = self.todt(sol[:] + [node], heap[:])

        return left or right

    def increasingTriplet(self, nums: list[int]) -> bool:
        size = len(nums)

        heap = []

        for i in range(size):
            heapq.heappush(heap, (nums[i], i))

        return self.todt([], heap)
    def increasingTriplet(self, nums: list[int]) -> bool:
        size = len(nums)

        minheap = []

        for i in range(size):
            heapq.heappush(minheap, (-nums[i], -i))
            if len(minheap) > 3:
                heapq.heappop(minheap)

            print(minheap)
        sol = []

        for i in range(3):
            node = heapq.heappop(minheap)
            sol.append((-node[0], -node[1]))

        return (sol[0][0] > sol[1][0] and sol[0][1] > sol[1][1]) and (
            sol[1][0] > sol[2][0] and sol[1][1] > sol[2][1]
        )


s = Solution()

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

# print(s.increasingTriplet([1, 2, 3, 4, 5]))
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.

# print(s.increasingTriplet([5, 4, 3, 2, 1]))
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

print(s.increasingTriplet([2, 1, 5, 0, 4, 6]))


# True
# [20,100,10,12,5,13]

# print(s.increasingTriplet([20, 100, 10, 12, 5, 13]))

# true
# [5,1,5,5,2,5,4]
# print(s.increasingTriplet([5, 1, 5, 5, 2, 5, 4]))
