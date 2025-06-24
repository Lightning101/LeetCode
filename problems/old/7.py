class Solution:
    def reverse(self, x: int) -> int:
        sign = x > 0
        reversed_num = 0

        x = abs(x)

        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10

        reversed_num *= sign

        if reversed_num < -(2**31) or reversed_num > (2**31 - 1):
            return 0
        return reversed_num


s = Solution()

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

print(s.reverse(123))

# Input: x = -123
# Output: -321
# Example 3:
print(s.reverse(-123))

# Input: x = 120
# Output: 21
print(s.reverse(120))
