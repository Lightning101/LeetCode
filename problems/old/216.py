class Solution:

    def findCombin(self, curr, total, used: set, k, target):
        if (total + curr) == target and k == len(used) + 1:
            return list(used) + [curr]

        if total + curr > target or len(used) + 1 > k:
            return None

        used.add(curr)
        ans = []
        for i in range(curr + 1, 10):
            if i not in used:
                if val := self.findCombin(i, total + curr, used, k, target):
                    if type(val[0]) is list:
                        ans.extend(val)
                    else:
                        ans.append(val)
        used.remove(curr)
        return ans

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        uLimit = sum([i for i in range(9, 9 - k - 1, -1)])

        if n > uLimit:
            return []
        ans = []
        for i in range(1, 10):
            # if i == n:
            #     if k == 1:
            #         ans.append([i])
            #     else:
            #         continue
            # else:
            if val := self.findCombin(i, 0, set(), k, n):
                if type(val[0]) is list:
                    ans.extend(val)
                else:
                    ans.append(val)
        return ans


s = Solution()


# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.

print(s.combinationSum3(3, 7))
# Example 2:

# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
print(s.combinationSum3(3, 9))
# Example 3:

# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
print(s.combinationSum3(4, 1))

# [[1,5],[2,4]]
print(s.combinationSum3(2, 6))
