class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if len(trust) == 0:
            if n == 1:
                return 1
            return -1

        # g = {}
        # sus = set()
        # for i in range(n):
        #     g[i + 1] = set()
        #     sus.add(i + 1)

        # for t in trust:
        #     if t[0] in sus:
        #         sus.remove(t[0])
        #     g[t[0]].add(t[1])

        # for p in sus:
        #     found = True
        #     for k in g.keys():
        #         if p != k and p not in g[k]:
        #             found = False
        #     if found:
        #         return p

        # g = [[False for _ in range(n)] for _ in range(n)]

        # for t in trust:
        #     g[t[0] - 1][t[1] - 1] = True

        # for i in range(n):
        #     if not any(g[i]):
        #         trusted = True
        #         for j in range(n):
        #             if j == i:
        #                 continue
        #             if not g[j][i]:
        #                 trusted = False
        #                 break
        #         if trusted:
        #             return i + 1

        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)

        for t in trust:
            out_degree[t[0]] += 1
            in_degree[t[1]] += 1

        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i

        return -1


s = Solution()

# 2
print(s.findJudge(2, [[1, 2]]))

# 3
print(s.findJudge(3, [[1, 3], [2, 3]]))


# -1
print(s.findJudge(3, [[1, 3], [2, 3], [3, 1]]))

#  -1
print(s.findJudge(4, [[1, 3], [1, 4], [2, 3]]))
