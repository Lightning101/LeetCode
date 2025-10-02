class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p = 0
        c = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[p] or c < 2:
                c = (nums[i] == nums[p]) * c
                nums[i], nums[p + 1] = nums[p + 1], nums[i]
                p += 1
            c += (c + 1) <= 2
        print(nums)
        return p +1


s = Solution()

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
# Example 2:


# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
