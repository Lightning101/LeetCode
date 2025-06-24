class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == (-1 << 31) and divisor == -1:
            return (1 << 31) - 1
        is_positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

        a = abs(dividend)
        b = abs(divisor)
        ans = 0
        if a == b:
            ans = 1
        else:
            while a >= b:
                i = 0
                while (b << i) <= a:
                    i += 1
                ans += 1 << (i - 1)
                a -= b << (i - 1)
        if not is_positive:
            return -ans
        return ans


s = Solution()


# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

print(s.divide(100, 13))
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.

# print(s.divide(7, -3))


# print(s.divide(-1, 1))
