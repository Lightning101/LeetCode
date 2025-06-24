from collections import deque


class Solution:

    def check_isvalid(self, node, size):
        return True if 0 <= node[0] < size[0] and 0 <= node[1] < size[1] else False

    def check_add(self, node, grid, size, seen, queue):
        if (
            node not in seen
            and self.check_isvalid(node, size)
            and grid[node[0]][node[1]] == "1"
        ):
            seen.add(node)
            queue.append(node)

    def bfs(self, size, source, grid, seen):
        queue = deque([source])

        while queue:
            node = queue.popleft()
            self.check_add((node[0] + 1, node[1]), grid, size, seen, queue)
            self.check_add((node[0] - 1, node[1]), grid, size, seen, queue)
            self.check_add((node[0], node[1] + 1), grid, size, seen, queue)
            self.check_add((node[0], node[1] - 1), grid, size, seen, queue)

    def dfs(self, source, grid, size, seen):
        if (
            source in seen
            or not self.check_isvalid(source, size)
            or grid[source[0]][source[1]] == "0"
        ):
            return
        seen.add(source)

        self.dfs((source[0] + 1, source[1]), grid, size, seen)
        self.dfs((source[0] - 1, source[1]), grid, size, seen)
        self.dfs((source[0], source[1] + 1), grid, size, seen)
        self.dfs((source[0], source[1] - 1), grid, size, seen)

    def numIslands(self, grid: list[list[str]]) -> int:
        seen = set()
        m = len(grid)
        n = len(grid[0])

        count = 0
        for x in range(m):
            for y in range(n):
                source = (x, y)
                if source not in seen and grid[x][y] == "1":
                    count += 1
                    seen.add(source)
                    self.bfs((m, n), source, grid, seen)
                    # self.dfs(source, grid, (m, n), seen)
        return count


s = Solution()


# 1
print(
    s.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)

# 3
print(
    s.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
