class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        size = len(nums)
        prod = None

        encounterdZeros = 0
        for i in range(size):
            if nums[i] == 0:
                encounterdZeros += 1
                continue
            if prod == None:
                prod = nums[i]
            else:
                prod *= nums[i]

        if encounterdZeros > 0:
            if encounterdZeros == 1:
                for i in range(size):
                    nums[i] = prod if nums[i] == 0 else 0
            else:
                nums[:] = [0 for i in range(size)]
        else:
            for i in range(size):
                nums[i] = prod // nums[i]

        return nums


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        size = len(nums)

        left = [1] * size
        right = [1] * size
        for i in range(1, size):
            left[i] = left[i - 1] * nums[i - 1]
            right[-i - 1] = right[-i] * nums[-i]

        output = []
        for i in range(size):
            output.append(left[i] * right[i])
        return output

# 14-10-2025
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        main = 1
        zeroCount = 0
        for n in nums:
            if n != 0:
                main *= n
            zeroCount += n == 0

        if zeroCount == 0:
            for i, v in enumerate(nums):
                nums[i] = 0 if (v == 0) else main // v
        elif zeroCount == 1:
            for i, v in enumerate(nums):
                nums[i] = main if (v == 0) else 0
        else:
            nums[:] = [0 for _ in range(len(nums))]
        return nums


s = Solution()


print(s.productExceptSelf([0, 0]))


s = Solution()
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# print(s.productExceptSelf([1, 2, 3, 4]))
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

print(s.productExceptSelf([-1, 1, 0, -3, 3, 0]))


# print(s.productExceptSelf([0, 2, 3, 4]))
