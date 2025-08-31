from collections import deque


# class Solution:

#     def minReorder(self, n: int, connections: list[list[int]]) -> int:

#         adj = [[(0, 0) for i in range(n)] for _ in range(n)]
#         for i in range(len(connections)):
#             s, r = connections[i]
#             adj[s][r] = (1, 1)
#             adj[r][s] = (1, 0)

#         st = deque()
#         st.append(0)
#         count = 0
#         visisted = set()
#         visisted.add(0)
#         while st:
#             s = st.popleft()

#             for i in range(n):
#                 if i not in visisted and i != s and adj[s][i][0] == 1:
#                     if adj[s][i][1] == 1:
#                         count += 1
#                     st.append(i)
#                     visisted.add(i)
#         return count


from collections import deque


class Solution:

    def minReorder(self, n: int, connections: list[list[int]]) -> int:

        adj = [[] for _ in range(n)]
        for i in range(len(connections)):
            s, r = connections[i]
            adj[s].append((r, 1))
            adj[r].append((s, 0))

        st = deque()
        st.append((0, -1))
        count = 0

        while st:
            c, p = st.popleft()
            for i in range(len(adj[c])):

                d, v = adj[c][i]
                if d != p:
                    count += v
                    st.append((d, c))
        return count


s = Solution()


# Example 1:


# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3

print(s.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
# Example 2:


# Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# Output: 2
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

print(s.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
# Example 3:

# Input: n = 3, connections = [[1,0],[2,0]]
# Output: 0

print(s.minReorder(3, [[1, 0], [2, 0]]))


# 6
print(
    s.minReorder(
        10, [[0, 1], [2, 1], [3, 2], [0, 4], [5, 1], [2, 6], [5, 7], [3, 8], [8, 9]]
    )
)
