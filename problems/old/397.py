from functools import lru_cache


class Solution:
    @lru_cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n < 1:
            return -1
        ans = 0
        if n % 2 == 0:
            ans = self.integerReplacement(n / 2)
        else:
            left = self.integerReplacement(n - 1)
            right = self.integerReplacement(n + 1)
            if left == -1:
                ans = right
            elif right == -1:
                ans = left
            else:
                ans = min(left, right)

        if ans > -1:
            return ans + 1


s = Solution()
# 8 -> 4 -> 2 -> 1 | 3
# print(s.integerReplacement(8))

# 7 -> 8 -> 4 -> 2 -> 1 | 4
# print(s.integerReplacement(7))

# 4 -> 2 -> 1 | 2
# print(s.integerReplacement(4))

# 17
print(s.integerReplacement(65535))
