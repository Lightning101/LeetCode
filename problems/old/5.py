class Solution:
    def checkPalidrom(self, s):
        size = len(s)
        p1 = size // 2 - 1
        p2 = size // 2

        if size % 2:
            p2 += 1

        while p1 >= 0 and p2 < len(s):
            p1 -= 1
            p2 += 1

        return s[p1:p2]

    def dfsPali(self, start, end, s, memo: dict):
        if (start, end) in memo:
            return memo[(start, end)]
        if start == end:
            return 1
        curr = self.checkPalidrom(s[start : end + 1])
        left = 0
        right = 0
        if start - 1 < -1:
            left = self.dfsPali(start - 1, end, s, memo)
        if end + 1 < len(s):
            right = self.dfsPali(start, end + 1, s, memo)
        memo[(start, end)] = max(curr, left, right)
        return memo[(start, end)]

    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        dp = [1] * size
        memo = {}
        for i in range(0, size):
            dp[i] = self.checkPalidrom(s[: i + 1])
            # dp[i] = self.dfsPali(0, i, s, memo)

        return max(dp)


s = Solution()

print(s.longestPalindrome("babad"))
# print(s.checkPalidrom("abba"[0:4]))
print(s.longestPalindrome("cbbd"))
