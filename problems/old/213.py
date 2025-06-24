class Solution:

    def robHouse(self, nums: list[int]) -> int:
        dp = [0]*3
        for i in range(len(nums)):
            ans1 = dp[1]
            ans2=dp[0]
            dp.append(nums[i] + max(ans1,ans2))
            dp = dp[1:]
        return max(dp[-1],dp[-2])
    
    def rob(self, nums: list[int]) -> int:
        size = len(nums)
        if(size <=2):
            return max(nums)

        return max(self.robHouse(nums[:size-1]),self.robHouse(nums[1:]))


s = Solution()

# 3
print(s.rob([2, 3, 2]))

# 4
print(s.rob([1, 2, 3, 1]))

# 3
print(s.rob([1, 2, 3]))

# 103
print(s.rob([1, 3, 1, 3, 100]))

# 3
print(s.rob([1, 2, 1, 1]))

# 3
print(s.rob([1, 1, 1, 2]))
