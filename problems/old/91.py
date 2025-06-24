from functools import lru_cache


class Solution:
    @lru_cache
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 1

        ch1 = int(s[0])
        if ch1 == 0:
            return 0

        if ch1 > 0 and ch1 < 3:
            ch2 = int(s[:2])
            if len(s) >= 2 and ch2 < 27:
                # print(f'Removed "{s[:1]}" and "{s[:2]}"')
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        # print(f'Removed "{s[:1]}"')
        return self.numDecodings(s[1:])


s = Solution()
# 2
# print(s.numDecodings("12"))

# 3
# print(s.numDecodings("226"))

# 0
print(s.numDecodings("06"))
