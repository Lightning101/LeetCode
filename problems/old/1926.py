from collections import deque


# class Solution:

#     def bfs(self, q, target, maze, visited, n, m):
#         spath = -1
#         while q:
#             x, y, c = q.popleft()
#             if (x, y) not in visited and maze[x][y] == ".":
#                 visited.add((x, y))
#                 for pos2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                     newPos = (x + pos2[0], y + pos2[1])
#                     if (
#                         0 > newPos[0]
#                         or newPos[0] >= n
#                         or 0 > newPos[1]
#                         or newPos[1] >= m
#                     ):
#                         continue
#                     if newPos == target:
#                         if spath == -1 or spath > (c + 1):
#                             spath = c + 1
#                     q.append(newPos + (c + 1,))

#         return spath

#     def nearestExit(self, maze, entrance) -> int:

#         startingPos = set()
#         n, m = len(maze), len(maze[0])
#         for i in range(n):
#             startingPos.add((i, 0, 0))
#             startingPos.add((i, m - 1, 0))

#         for i in range(m):
#             startingPos.add((0, i, 0))
#             startingPos.add((n - 1, i, 0))

#         start = (entrance[0], entrance[1], 0)
#         if start in startingPos:
#             startingPos.remove(start)
#         if len(startingPos) == 0:
#             return -1

#         visited = set()
#         q = deque(startingPos)
#         return self.bfs(q, start[:2], maze, visited, n, m)

from collections import deque
class Solution:

    def bfs(self,start, maze, visited, n, m):
        q = deque([start+(0,)])
        while q:
            x, y, c = q.popleft()
            if (x, y) not in visited:
                visited.add((x, y))
                for pos2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newPos = (x + pos2[0], y + pos2[1])
                    if (
                        0 > newPos[0]
                        or newPos[0] >= n
                        or 0 > newPos[1]
                        or newPos[1] >= m
                        or maze[newPos[0]][newPos[1]] == '+'
                    ):
                        continue
                    if newPos != start and (newPos[0] ==0 or newPos[1] == 0 or newPos[0] == n -1 or newPos[1] == m-1):
                        return c+1
                    q.append(newPos + (c + 1,))

        return -1

    def nearestExit(self, maze, entrance) -> int:
        n, m = len(maze), len(maze[0])
        visited = set()
        return self.bfs((entrance[0], entrance[1]), maze, visited, n, m)

s = Solution()


# Example 1:


# Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
# Output: 1
# Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
# Initially, you are at the entrance cell [1,2].
# - You can reach [1,0] by moving 2 steps left.
# - You can reach [0,2] by moving 1 step up.
# It is impossible to reach [2,3] from the entrance.
# Thus, the nearest exit is [0,2], which is 1 step away.

print(
    s.nearestExit(
        [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]
    )
)
# Example 2:


# Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
# Output: 2
# Explanation: There is 1 exit in this maze at [1,2].
# [1,0] does not count as an exit since it is the entrance cell.
# Initially, you are at the entrance cell [1,0].
# - You can reach [1,2] by moving 2 steps right.
# Thus, the nearest exit is [1,2], which is 2 steps away.

print(s.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1,0]))
# Example 3:


# Input: maze = [[".","+"]], entrance = [0,0]
# Output: -1
# Explanation: There are no exits in this maze.
print(s.nearestExit([[".","+"]], [0,0]))


print(s.nearestExit([["+"],["."]], [1,0]))

print(
    s.nearestExit(
        [
            ["+", ".", "+", "+", "+", "+", "+"],
            ["+", ".", "+", ".", ".", ".", "+"],
            ["+", ".", "+", ".", "+", ".", "+"],
            ["+", ".", ".", ".", "+", ".", "+"],
            ["+", "+", "+", "+", "+", ".", "+"],
        ],
        [0, 1],
    )
)
