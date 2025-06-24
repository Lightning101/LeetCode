class Solution:
    def palce_queens(self, r, op, ans, placed, n):
        if r == n:
            temp = []
            for j in op:
                temp.append("".join(j))
            ans.append(temp)
            return

        for c in range(n):
            pos = c
            diag = r + c
            ndiag = r - c

            if pos in placed[0] or diag in placed[1] or ndiag in placed[2]:
                continue

            placed[0].add(pos)
            placed[1].add(diag)
            placed[2].add(ndiag)
            op.append("." * c + "Q" + "." * (n - c - 1))
            self.palce_queens(r + 1, op, ans, placed, n)

            op.pop()
            placed[0].remove(pos)
            placed[1].remove(diag)
            placed[2].remove(ndiag)

    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        self.palce_queens(0, [], ans, [set(), set(), set()], n)
        return ans


s = Solution()
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
print(s.solveNQueens(4))

# Example 2:

# Input: n = 1
# Output: [["Q"]]

print(s.solveNQueens(1))
