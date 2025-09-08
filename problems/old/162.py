class Solution:

    # def findPeakElement(self, nums: list[int]) -> int:

    #     size = len(nums)
    #     left = 0
    #     right = size - 1

    #     while left < right:
    #         mid = (left + right) // 2

    #         if (
    #             (0 < mid < size - 1 and nums[mid - 1] < nums[mid] > nums[mid + 1])
    #             or (mid == 0 and nums[mid] > nums[mid + 1])
    #             or (mid == size - 1 and nums[mid] > nums[mid - 1])
    #         ):
    #             return mid
    #         elif 0 < mid and nums[mid] < nums[mid - 1]:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return left

    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            print(f"mid: {nums[mid]} l:{left}, m:{mid}, r:{right}")
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        print(f"mid: {nums[mid]} l:{left}, m:{mid}, r:{right}")
        return left


s = Solution()


# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# print(s.findPeakElement([1, 2, 3, 1]))

# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
# print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))


# print(s.findPeakElement([1, 2, 1, 2, 2, 2, 2]))
