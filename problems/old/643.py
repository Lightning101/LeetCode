class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        ans = sum(nums[:k])
        rolling_avg = ans
        for i in range(0, len(nums) - k):
            rolling_avg = rolling_avg - nums[i] + nums[i + k]
            if ans < rolling_avg:
                ans = rolling_avg

        return ans / k


s = Solution()
# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))

# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

print(s.findMaxAverage([5], 1))


# 4.00000
print(s.findMaxAverage([0, 4, 0, 3, 2], 1))
