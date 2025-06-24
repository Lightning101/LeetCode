class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        count = 0
        open_count = 0
        for c in s:
            if c == "(":
                open_count += 1
            elif c == ")" and open_count > 0:
                open_count -= 1
            else:
                count += 1

        return count + open_count


s = Solution()


# Example 1:

# Input: s = "())"
# Output: 1

print(s.minAddToMakeValid("())"))
# Example 2:
# Input: s = "((("
# Output: 3
print(s.minAddToMakeValid("((("))


# 4
print(s.minAddToMakeValid("()))(("))
