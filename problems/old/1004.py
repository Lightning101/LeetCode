from collections import deque


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:

        size = len(nums)
        max_size = 0
        p1, p2 = 0, 0

        zero_loc = deque()

        while p2 < size:
            if nums[p2] == 1 or len(zero_loc) < k:
                if nums[p2] == 0:
                    zero_loc.append(p2)
                count = p2 - p1 + 1
                max_size = count if (count > max_size) else max_size
                p2 += 1
            else:

                if len(zero_loc) > 0:
                    p1 = zero_loc.popleft() + 1
                else:
                    while p2 < size and nums[p2] != 1:
                        p2 += 1
                    p1 = p2

        return max_size


s = Solution()


# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

print(s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))


print(s.longestOnes([0, 0, 1, 1, 1, 0, 0], 0))
