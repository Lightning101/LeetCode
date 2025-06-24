from collections import deque


class Solution:
    def Get4Points(self, x, y, i):
        if i % 2 == 0:
            x = x - 1 + i
        else:
            y = y - 2 + i
        return x, y

    # def BFS(self, x, y, m, n, mat):
    #     if mat[x][y] == 0:
    #         return [(x, y)]
    #     ans = (-1, -1)
    #     st = deque([[(x, y)]])
    #     searchedSet = set([(x, y)])
    #     lvl = 1
    #     while st:
    #         for _ in range(len(st)):
    #             path = st.popleft()
    #             x2, y2 = path[-1]

    #             if mat[x2][y2] == 0:
    #                 return path

    #             searchedSet.add((x2, y2))
    #             for i in range(4):
    #                 x3, y3 = self.Get4Points(x2, y2, i)
    #                 if (
    #                     x3 < 0
    #                     or x3 >= m
    #                     or y3 < 0
    #                     or y3 >= n
    #                     or (x3, y3) in searchedSet
    #                 ):
    #                     continue
    #                 st.append(path[:] + [(x3, y3)])
    #             lvl += 1
    #     return ans

    # Working
    # def DFS(self, x, y, m, n, mat, res):
    #     if x<0 or x >= m or y < 0 or y >= n:
    #         return m * n
    #     elif res[x][y] == 0:
    #         return 0
    #     elif(res[x][y] == -1):
    #         print(x,y)
    #         res[x][y] = m *n
    #         ans = m * n
    #         for i in range(4):
    #             x2, y2 = self.Get4Points(x, y, i)
    #             ans = min(self.DFS(x2, y2, m, n, mat, res), ans)
    #         res[x][y] = ans +1
    #         return res[x][y]
    #     else:
    #         return res[x][y]

    # (x2<0 or x2 >= m or y2 < 0 or y2 >= n) False
    # def DFS(self, x, y, m, n, mat, res, st: set):
    #     if mat[x][y] == 0:
    #         return 0
    #     elif((x,y) not in st):
    #         print(x,y)
    #         st.add((x,y))
    #         ans = -1
    #         for i in range(4):
    #             x2, y2 = self.Get4Points(x, y, i)
    #             if(x2 >=0 and x2 < m and y2 >= 0 and y2 < n):
    #                 newVal = None
    #                 if(x2<x or (x2==x and y2 <y)):
    #                     newVal = res[x2][y2]
    #                 else:
    #                     newVal = self.DFS(x2, y2, m, n, mat, res,st)
    #                 if(ans == -1):
    #                     ans = newVal
    #                 else:
    #                     ans = min(newVal, ans)
    #         res[x][y] = ans +1
    #     return res[x][y]

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])

        st =deque()
        ans = []
        for x in range(m):
            row = []
            for y in range(n):
                val = n*m
                if(mat[x][y] == 0):
                    val = 0
                    st.append((x,y))
                row.append(val)
            ans.append(row)
        
        while(st):
            for _ in range(len(st)):
                x,y = st.popleft()
                for i in range(4):
                    x2,y2 = self.Get4Points(x,y,i)
                    if(x2>-1 and x2 < m and y2 > -1 and y2 < n):
                        if(ans[x][y] +1 < ans[x2][y2]):
                            ans[x2][y2] = ans[x][y] + 1
                            st.append((x2,y2))

        return ans



s = Solution()

# [[0,0,0],[0,1,0],[0,0,0]]
# print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

#  [[0,0,0],[0,1,0],[1,2,1]]
# print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))


# [[0,0,0],[0,1,0],[0,0,0]]
print(s.updateMatrix([[0, 1, 1], [1, 1, 1], [1, 1, 1]]))


# graph is in adjacent list representation
# graph = {
#     "1": ["2", "3", "4"],
#     "2": ["5", "6"],
#     "5": ["9", "10"],
#     "4": ["7", "8"],
#     "7": ["11", "12"],
# }


# def bfs(graph, start, end):
#     # maintain a queue of paths
#     queue = []
#     # push the first path into the queue
#     queue.append([start])
#     while queue:
#         # get the first path from the queue
#         path = queue.pop(0)
#         # get the last node from the path
#         node = path[-1]
#         # path found
#         if node == end:
#             return path
#         # enumerate all adjacent nodes, construct a
#         # new path and push it into the queue
#         for adjacent in graph.get(node, []):
#             new_path = list(path)
#             new_path.append(adjacent)
#             queue.append(new_path)


# print(bfs(graph, "1", "11"))
