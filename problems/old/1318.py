# class Solution:
#     def minFlips(self, a: int, b: int, c: int) -> int:
#         count = 0
#         bitMask = 1
#         while c > 0 or a > 0 or b > 0:
#             aActual = a & bitMask
#             bActual = b & bitMask
#             orResult = aActual | bActual

#             cExpected = c & bitMask
#             if orResult != cExpected:
#                 if orResult and not cExpected:
#                     count += aActual + bActual
#                 else:
#                     count += 1
#             c >>= 1
#             a >>= 1
#             b >>= 1
#         return count
    
# optimized after looking at solution
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while c or a or b:
            if c & 1:
                count +=  not ((a & 1) | (b & 1))
            else:
                count += (a & 1) + (b & 1)
            c >>= 1
            a >>= 1
            b >>= 1
        return count


s = Solution()


# Example 1:


# Input: a = 2, b = 6, c = 5
# a --> 010
# b --> 110
# c --> 101
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

# print(s.minFlips(2, 6, 5))
# Example 2:

# Input: a = 4, b = 2, c = 7
# Output: 1

# print(s.minFlips(4, 2, 7))
# Example 3:

# Input: a = 1, b = 2, c = 3
# Output: 0
# print(s.minFlips(1, 2, 3))

# a --> 0101
# b --> 0010
# b --> 1000
# 4
# print(s.minFlips(5, 2, 8))


# a --> 1000
# b --> 0011
# c --> 0101
# 3
print(s.minFlips(8, 3, 5))
