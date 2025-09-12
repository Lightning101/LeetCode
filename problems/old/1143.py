from functools import cache


# class Solution:
#     @cache
#     def lcs(self, i, j):
#         if i == -1 or j == -1:
#             return 0
#         else:
#             if self.text1[i] == self.text2[j]:
#                 return 1 + self.lcs(i - 1, j - 1)
#             else:
#                 return max(self.lcs(i - 1, j) ,self.lcs(i, j - 1))

#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         self.text1 = text1
#         self.text2 = text2
#         n = len(text1)
#         m = len(text2)
#         return self.lcs(n - 1, m - 1)

# class Solution:
#     def lcs(self, i, j,t1,t2,memo):
#         if((i,j) in memo ):
#             return memo[(i,j)]
#         if i == -1 or j == -1:
#             return 0
#         else:
#             if t1[i] == t2[j]:
#                 memo[(i,j)] = 1 + self.lcs(i - 1, j - 1,t1,t2,memo)
#             else:
#                 memo[(i,j)]= max(self.lcs(i - 1, j,t1,t2,memo) ,self.lcs(i, j - 1,t1,t2,memo))
#             return memo[(i,j)]

#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n = len(text1)
#         m = len(text2)
#         return self.lcs(n - 1, m - 1,text1,text2,{})
    


# class Solution:


#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n = len(text1)
#         m = len(text2)
#         dp = [[0] * (m+1) for _ in range(n+1)]
#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 if(text1[i-1] == text2[j-1]):
#                     dp[i][j] = dp[i-1][j-1]+1
#                 else:
#                     dp[i][j]=max(dp[i-1][j],dp[i][j-1])
#         return dp[n][m]
        

class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        p = [0] * (m + 1)

        for i in range(1, n + 1):
            c = [0] * (m + 1)
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    c[j] = p[j - 1] + 1
                else:
                    c[j] = max(p[j], c[j - 1])
            p = c
        return c[m]


s = Solution()

# Example 1:

# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

print(s.longestCommonSubsequence("abcde", "ace"))
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
print(s.longestCommonSubsequence("abc", "abc"))

# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
print(s.longestCommonSubsequence("abc", "def"))

# 2
print(s.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))

# 5
print(s.longestCommonSubsequence("hofubmnylkra", "pqhgxgdofcvmr"))

