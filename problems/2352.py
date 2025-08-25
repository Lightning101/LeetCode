from collections import defaultdict


# class Solution:
#     def equalPairs(self, grid: list[list[int]]) -> int:

#         size = len(grid)

#         pairs = defaultdict(lambda: (0, 0))
#         for x in range(size):
#             row = ()
#             column = ()
#             for y in range(size):
#                 row += (grid[x][y],)
#                 column += (grid[y][x],)

#             pairs[column] = (pairs[column][0], pairs[column][1] + 1)
#             pairs[row] = (pairs[row][0]+ 1, pairs[row][1] )

#         ans = 0

#         for k in pairs.keys():
#             ans += pairs[k][0] * pairs[k][1]

#         return ans


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:

        size = len(grid)

        pairs = defaultdict(lambda: (0, 0))
        ans = 0

        for x in range(size):
            row = ()
            column = ()
            for y in range(size):
                row += (grid[x][y],)
                column += (grid[y][x],)

            ans -= pairs[column][0] * pairs[column][1]
            pairs[column] = (pairs[column][0], pairs[column][1] + 1)
            ans += pairs[column][0] * pairs[column][1]

            ans -= pairs[row][0] * pairs[row][1]
            pairs[row] = (pairs[row][0] + 1, pairs[row][1])
            ans += pairs[row][0] * pairs[row][1]

        # for k in pairs.keys():
        #     ans += pairs[k][0] * pairs[k][1]

        return ans


s = Solution()


# Example 1:


# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]

print(s.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
# Example 2:


# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

print(s.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
