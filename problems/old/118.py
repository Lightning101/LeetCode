class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1]]
        for row_len in range(2, numRows + 1):
            next_row = [1]
            for i in range(1, row_len - 1):
                next_row.append(ans[-1][i - 1] + ans[-1][i])
            next_row.append(1)
            ans.append(next_row)

        return ans

s = Solution()
# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# print([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
print(s.generate(5))
# Example 2:

# Input: numRows = 1
# Output: [[1]]
# print(s.generate(1))

print(s.generate(8))