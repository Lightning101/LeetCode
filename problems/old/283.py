# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         p0, p1 = 0, 0
#         size = len(nums)
#         while p0 < size and nums[p0] != 0:
#             p0 += 1

#         p1 = p0 + 1

#         while p1 < size and p0 < size:
#             if nums[p1] != 0:
#                 nums[p0], nums[p1] = nums[p1], nums[p0]
#                 while p0 < size and nums[p0] != 0:
#                     p0 += 1
#             p1 += 1


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        zero_ele = 0

        for i in range(0,size):
            if(nums[i] != 0):
                nums[zero_ele],nums[i] = nums[i],nums[zero_ele]
                zero_ele+=1


s = Solution()

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# nums = [0, 1, 0, 3, 12]

# Example 2:

# Input: nums = [0]
# Output: [0]
# nums = [0]
# s.moveZeroes(nums)
# print(nums)

nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]


s.moveZeroes(nums)
print(nums)
