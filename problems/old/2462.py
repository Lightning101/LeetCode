import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        ans = 0
        costSize = len(costs)
        rightStart = costSize - max(candidates, costSize - candidates)

        hp = []

        for i in range(candidates):
            hp.append((costs[i], 0))

        for i in range(costSize - rightStart, costSize):
            hp.append((costs[i], 1))

        heapq.heapify(hp)

        p1 = candidates
        p2 = costSize - candidates - 1

        for _ in range(k):
            ele = heapq.heappop(hp)
            ans += ele[0]
            if not ele[1] and p1 <= p2:
                heapq.heappush(hp, (costs[p1], 0))
                p1 += 1
            elif ele[1] and p1 <= p2:
                heapq.heappush(hp, (costs[p2], 1))
                p2 -= 1

        return ans


s = Solution()

# print("===== Ideal =====")
# data = [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58]

# for _ in range(11):
#     print(f"""data: {data}
#     left: {data[:2]}
#     right: {data[-2:]}
#     """
#     )
#     small = min(min(data[:2]), min(data[-2:]))
#     print(f"Smallest Ele {small}")
#     data.remove(small)


# print("===== Actual =====")


# Example 1:

# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
# - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
# - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
# The total hiring cost is 11.

print(s.totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4))
# Example 2:

# Input: costs = [1,2,4,1], k = 3, candidates = 3
# Output: 4
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
# - In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
# - In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
# The total hiring cost is 4.

print(s.totalCost([1, 2, 4, 1], 3, 3))

# 423
print(
    s.totalCost([31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58], 11, 2)
)
