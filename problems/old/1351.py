class Solution:
    def bs(self, grid, m, n):
        l, r = 0, n
        while l < n and l <= r:
            mid = (l + r) // 2
            if grid[m][mid] < 0:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def countNegatives(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        ans = 0
        for i in range(len(grid)):
            # print(f"grid: {grid[i]} -> {self.bs(grid, i, n)}")
            ans += n - self.bs(grid, i, n)
        return ans


s = Solution()


# Example 1:

# Input: grid =
# [
# [4,3,2,-1],
# [3,2,1,-1],
# [1,1,-1,-2],
# [-1,-1,-2,-3]
# ]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

print(
    s.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
)
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0

# print(s.countNegatives([[3, 2], [1, 0]]))
