class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1, len2 = len(nums1), len(nums2)
        left, right = 0, len1
        print(f"len1: {len1} len2: {len2}")
        print(f"left: {left} right: {right}")

        while left <= right:
            part1 = (left + right) // 2
            part2 = (len1 + len2 + 1) // 2 - part1

            max_left1 = float("-inf") if part1 == 0 else nums1[part1 - 1]
            min_right1 = float("inf") if part1 == len1 else nums1[part1]
            max_left2 = float("-inf") if part2 == 0 else nums2[part2 - 1]
            min_right2 = float("inf") if part2 == len2 else nums2[part2]

            print(f"part1: {part1} part2: {part2}")
            print(
                f"max_left1: {max_left1} max_left2: {max_left2} min_right1: {min_right1}  min_right2: {min_right2} "
            )
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (len1 + len2) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                right = part1 - 1
            else:
                left = part1 + 1


s = Solution()


# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# print(s.findMedianSortedArrays([1, 3], [2]))

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# print(s.findMedianSortedArrays([1, 2], [3, 4]))


print(s.findMedianSortedArrays([1, 3, 8], [7, 9, 10, 11]))
