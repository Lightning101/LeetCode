class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        idx = m + n - 1
        while p1 != -1 and p2 != -1:
            if nums1[p1] > nums2[p2]:
                nums1[idx] = nums1[p1]
                p1 -= 1
            else:
                nums1[idx] = nums2[p2]
                p2 -= 1
            idx -= 1

        if p1 == -1:
            nums1[: idx + 1] = nums2[: p2 + 1]
        if p2 == -1:
            nums1[: idx + 1] = nums1[: p1 + 1]

        return nums1


s = Solution()
# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
print(s.merge([1], 1, [], 0))
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
print(s.merge([0], 0, [1], 1))


print(s.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
