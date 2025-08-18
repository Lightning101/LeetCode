# class Solution:
#     def maxOperations(self, nums: list[int], k: int) -> int:
#         nums.sort()
#         p1 = 0
#         p2 = len(nums) - 1

#         count = 0
#         s = set()
#         while p1 < p2:
#             if (nums[p1], nums[p2]) in s:
#                 count += 1
#                 p1 += 1
#                 p2 -= 1
#             elif nums[p1] + nums[p2] > k:
#                 p2 -= 1
#             elif nums[p1] + nums[p2] < k:
#                 p1 += 1
#             else:
#                 s.add((nums[p1], nums[p2]))
#                 count += 1
#                 p1 += 1
#                 p2 -= 1

#         return count



# from collections import defaultdict


# class Solution:
#     def maxOperations(self, nums: list[int], k: int) -> int:
#         compliments = defaultdict(int)
#         count = 0
#         for i in range(len(nums)):
#             n = nums[i]
#             c = k - nums[i]

#             if c in compliments and compliments[c] > 0:
#                 count += 1
#                 compliments[c] -= 1
#             else:
#                 compliments[n] += 1

#         return count
    

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        compliments = {}
        count = 0
        for i in range(len(nums)):
            n = nums[i]
            c = k - nums[i]

            if c in compliments and compliments[c] > 0:
                count += 1
                compliments[c] -= 1
            else:
                if n in compliments:
                    compliments[n] += 1
                else:
                    compliments[n] = 1

        return count


s = Solution()


# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
print(s.maxOperations([1, 2, 3, 4], 5))
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.

print(s.maxOperations([3, 1, 3, 4, 3], 6))


# [2,2,2,3,1,1,4,1], 4
# 2

print(s.maxOperations([2, 2, 2, 3, 1, 1, 4, 1], 4))
