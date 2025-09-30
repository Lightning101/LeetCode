class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0
            
        size = len(nums)
        p = size - 1
        i = 0
        while i < p:
            if nums[i] == val:
                nums[i], nums[p] = nums[p], nums[i]
                p -= 1
            else:
                i += 1
        return i + (nums[i] != val)


s = Solution()

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
print(s.removeElement([3, 2, 2, 3], 3))
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(s.removeElement([3, 3], 3))
