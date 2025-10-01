class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        size = len(nums)
        p = 1
        for i in range(1, size):
            if nums[p - 1] != nums[i]:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        return p
