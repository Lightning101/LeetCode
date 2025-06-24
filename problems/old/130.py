from collections import deque


class Solution:

    def check_add(self, node, size, board, queue, safe):
        if (
            not node in safe
            and 0 <= node[0] < size
            and 0 <= node[1] < size
            and board[node[0]][node[1]] == "O"
        ):
            queue.append(node)
            safe.add(node)

    def bfs(self, g, source, safe, size):
        queue = deque(source)

        while queue:
            (x, y) = queue.popleft()
            self.check_add((x + 1, y), size, g, queue, safe)
            self.check_add((x - 1, y), size, g, queue, safe)
            self.check_add((x, y + 1), size, g, queue, safe)
            self.check_add((x, y - 1), size, g, queue, safe)

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        safe = set()
        sources = set()

        for i in range(m):
            if board[0][i] == "O":
                safe.add((0, i))
                sources.add((0, i))
            if board[n - 1][i] == "O":
                safe.add((n - 1, i))
                sources.add((n - 1, i))

        for i in range(n):
            if board[i][0] == "O":
                safe.add((i, 0))
                sources.add((i, 0))

            if board[i][m - 1] == "O":
                safe.add((i, m - 1))
                sources.add((i, m - 1))

        self.bfs(board, sources, safe, n)
        for i in range(n):
            for j in range(m):
                if (i, j) not in safe:
                    board[i][j] = "X"


s = Solution()

# board = [
#     ["X", "X", "X", "X"],
#     ["X", "O", "O", "X"],
#     ["X", "X", "O", "X"],
#     ["X", "O", "X", "X"],
# ]
# s.solve(board)
# print(board)


# board = [["X"]]
# s.solve(board)
# print(board)
board = [
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
]
print("==== Input ====")
for row in board:
    print(row)

s.solve(board)
print("==== Output ====")
for row in board:
    print(row)
