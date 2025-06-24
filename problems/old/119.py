# class Solution:
#     def getRow(self, rowIndex: int) -> list[int]:
#         ans = [1]
#         for i in range(1, rowIndex):
#             curr = [1]
#             for j in range(0, len(ans) - 1):
#                 curr.append(ans[j] + ans[j + 1])
#             if i % 2:
#                 curr.append(ans[-1] * 2)

#             ans = curr
#         if rowIndex % 2:
#             return ans + ans[::-1]

#         return ans + ans[: len(ans) - 1][::-1]


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]

        for i in range(1, (rowIndex + 2) // 2):
            next_element = row[i - 1] * (rowIndex - i + 1) // i
            row.append(next_element)

        if rowIndex % 2:
            return row + row[::-1]

        return row + row[: len(row) - 1][::-1]


s = Solution()

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# for i in range(7):
#     print(s.getRow(i))

# Input: rowIndex = 0
# Output: [1]
# Example 3:
# print(s.getRow(0))
# Input: rowIndex = 1
# Output: [1,1]
print(s.getRow(5))
