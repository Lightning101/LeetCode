from collections import deque


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        sources = set()

        for i in range(m):
            if grid[0][i] == 1:
                grid[0][i] = 0
                sources.add((0, i))
            if grid[n - 1][i] == 1:
                grid[n - 1][i] = 0
                sources.add((n - 1, i))

        for i in range(n):
            if grid[i][0] == 1:
                grid[i][0] = 0
                sources.add((i, 0))

            if grid[i][m - 1] == 1:
                grid[i][m - 1] = 0
                sources.add((i, m - 1))

        self.bfs(grid, sources, n)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        return count

    def check_add(self, node, size, grid, queue):
        if 0 <= node[0] < size and 0 <= node[1] < size and grid[node[0]][node[1]] == 1:
            queue.append(node)
            grid[node[0]][node[1]] = 0

    def bfs(self, g, source, size):
        queue = deque(source)

        while queue:
            (x, y) = queue.popleft()
            self.check_add((x + 1, y), size, g, queue)
            self.check_add((x - 1, y), size, g, queue)
            self.check_add((x, y + 1), size, g, queue)
            self.check_add((x, y - 1), size, g, queue)


s = Solution()
# 3
# print(s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))

# 0
print(s.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))