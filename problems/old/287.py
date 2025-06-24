class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow


s = Solution()


# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
print(s.findDuplicate([1, 3, 4, 2, 2]))


# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:
# print(s.findDuplicate([3, 1, 3, 4, 2]))

# Input: nums = [3,3,3,3,3]
# Output: 3
# print(s.findDuplicate([3, 3, 3, 3, 3]))
