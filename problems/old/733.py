from collections import deque


class Solution:
    def check_add(self, graph, node, size, target, final, queue):
        if (
            0 <= node[0] < size[0]
            and 0 <= node[1] < size[1]
            and graph[node[0]][node[1]] == target
        ):
            queue.append((node[0], node[1]))
            graph[node[0]][node[1]] = final

    def dfs(self, graph, node, target, final, size):
        if (
            0 <= node[0] < size[0]
            and 0 <= node[1] < size[1]
            and graph[node[0]][node[1]] == target
        ):
            graph[node[0]][node[1]] = final
            (sx, sy) = node
            self.dfs(graph, (sx + 1, sy), target, final, size)
            self.dfs(graph, (sx - 1, sy), target, final, size)
            self.dfs(graph, (sx, sy + 1), target, final, size)
            self.dfs(graph, (sx, sy - 1), target, final, size)

    def bfs(self, graph, source, final):
        queue = deque([source])
        target = graph[source[0]][source[1]]
        graph[source[0]][source[1]] = final
        size = (len(graph), len(graph[0]))
        while queue:
            (sx, sy) = queue.popleft()
            self.check_add(graph, (sx + 1, sy), size, target, final, queue)
            self.check_add(graph, (sx - 1, sy), size, target, final, queue)
            self.check_add(graph, (sx, sy + 1), size, target, final, queue)
            self.check_add(graph, (sx, sy - 1), size, target, final, queue)

    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        if image[sr][sc] != color:
            self.bfs(image, (sr, sc), color)
            # size = (len(image), len(image[0]))
            # self.dfs(image, (sr, sc), image[sr][sc], color, size)
        return image


s = Solution()

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

# Output: [[2,2,2],[2,2,0],[2,0,1]]
# print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))


# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

# Output: [[0,0,0],[0,0,0]]

# print(s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))


print(s.floodFill([[0, 0, 0], [0, 1, 0]], 1, 1, 2))
