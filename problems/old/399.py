from collections import defaultdict


class Solution:

    def DFS(self, node, target, adj_list, visited, cost=1.0):
        if node == target:
            return cost

        if node not in adj_list:
            return -1

        visited.add(node)
        paths = []
        for n in adj_list[node]:
            if n[0] not in visited and (
                (p := self.DFS(n[0], target, adj_list, visited, cost * n[1])) != -1
            ):
                return p
        return -1

    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        adj_list = defaultdict(list)

        for i in range(len(equations)):
            adj_list[equations[i][0]].append((equations[i][1], values[i]))
            adj_list[equations[i][1]].append((equations[i][0], 1 / values[i]))

        ans = []
        for query in queries:
            if not (query[0] in adj_list and query[1] in adj_list):
                ans.append(-1.0)
            else:
                visited = set()
                ans.append(self.DFS(query[0], query[1], adj_list, visited))

        return ans


s = Solution()


# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0

# print(
#     s.calcEquation(
#         [["a", "b"], ["b", "c"]],
#         [2.0, 3.0],
#         [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
#     )
# )
# Example 2:

# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]


# print(
#     s.calcEquation(
#         [["a", "b"], ["b", "c"], ["bc", "cd"]],
#         [1.5, 2.5, 5.0],
#         [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
#     )
# )
# Example 3:

# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]


# print(
#     s.calcEquation(
#         [["a", "b"]],
#         [0.5],
#         [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
#     )
# )


# print(
#     s.calcEquation(
#         [["a", "b"], ["c", "d"]],
#         [1.0, 1.0],
#         [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]],
#     )
# )

# [360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000]
print(
    s.calcEquation(
        [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
        [3.0, 4.0, 5.0, 6.0],
        [
            ["x1", "x5"],
            ["x5", "x2"],
            ["x2", "x4"],
            ["x2", "x2"],
            ["x2", "x9"],
            ["x9", "x9"],
        ],
    )
)
