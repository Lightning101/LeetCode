class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        p1, p2 = 0, n - 1
        ans = min(height[p1], height[p2]) * (p2 - p1)

        while p1 <= p2:

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

            new_area = min(height[p1], height[p2]) * (p2 - p1)
            if ans < new_area:
                ans = new_area

        return ans


s = Solution()

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# Example 2:

# Input: height = [1,1]
# Output: 1
print(s.maxArea([1, 1]))
