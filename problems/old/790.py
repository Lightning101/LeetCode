from functools import lru_cache


class Solution:
    @lru_cache
    def f(self, k):
        if k <= 2:
            return k
        return (self.f(k - 1) + self.f(k - 2) + 2 * self.p(k - 1)) % 1_000_000_007

    @lru_cache
    def p(self, k):
        if k == 2:
            return 1
        return self.f(k - 2) + self.p(k - 1)

    def numTilings(self, n: int) -> int:
        return self.f(n)


s = Solution()

# Example 1:


# Input: n = 3
# Output: 5
# Explanation: The five different ways are shown above.

print(s.numTilings(3))
# Example 2:

# Input: n = 1
# Output: 1
# print(s.numTilings(1))


# 11
print(s.numTilings(4))

# 24
print(s.numTilings(5))

# print(s.numTilings(1000))
