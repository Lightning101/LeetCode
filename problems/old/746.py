class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        size = len(cost)
        if size <= 2:
            return min(cost)

        p2 = cost[0]
        p1 = cost[1]

        for i in range(2, size):
            temp = min(p1, p2) + cost[i]
            p2 = p1
            p1 = temp
        return min(p1,p2)



s = Solution()
# 15
print(s.minCostClimbingStairs([10,15,20]))
# 6
# print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

# 2
# print(s.minCostClimbingStairs([0, 2, 2, 1]))
