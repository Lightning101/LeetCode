from queue import PriorityQueue
import math

# class Solution:
#     def bfs(self, source, graph, visited):

#         queue = PriorityQueue()
#         queue.put((0, source))
#         longest_delay = -1
#         while not queue.empty():
#             [w, s] = queue.get()
#             longest_delay = w
#             for adj in graph[s]:
#                 if not visited[adj[0]]:
#                     queue.put((w + adj[1], adj[0]))
#                     visited[adj[0]] = True
#         return longest_delay

#     def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
#         adj_list = {i: [] for i in range(n)}

#         for [s, d, w] in times:
#             adj_list[s - 1].append((d - 1, w))
#         visited = {i: False for i in range(n)}

#         longest_delay = self.bfs(k - 1, adj_list, visited)
#         if not any(visited.values()):
#             return -1
#         return longest_delay


class Solution:
    def bfs(self, source, graph, distances):
        queue = PriorityQueue()
        queue.put((0, source))
        while not queue.empty():
            [w, s] = queue.get()
            if distances[s] < w:
                continue
            print(f"wieght at node {s} is {w}")
            for adj in graph[s]:
                if distances[adj[0]] > w + adj[1]:
                    queue.put((w + adj[1], adj[0]))
                    distances[adj[0]] = w + adj[1]

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_list = {i: [] for i in range(n)}

        for [s, d, w] in times:
            adj_list[s - 1].append((d - 1, w))
        distances = {i: math.inf for i in range(n)}
        distances[k - 1] = 0

        self.bfs(k - 1, adj_list, distances)
        # Check distance
        max_distance = 0
        for distance in distances.values():
            if distance == math.inf:
                return -1
            if max_distance < distance:
                max_distance = distance
        return max_distance


s = Solution()


# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:
print(s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:
print(s.networkDelayTime([[1, 2, 1]], 2, 1))

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
print(s.networkDelayTime([[1, 2, 1]], 2, 2))

# 2
print(s.networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 2]], 3, 1))
