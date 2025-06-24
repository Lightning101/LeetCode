class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        size = len(nums)
        dp = [0]* size
        dp[0] = 1
        
        for i in range(1,size):
            ans = 0
            for j in range(i-1,-1,-1):
                if(nums[i]>nums[j]):
                    if(ans<dp[j]):
                        ans = dp[j]
            dp[i] = ans +1
        return max(dp)
    

    

s = Solution()
# 4
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
# 4
print(s.lengthOfLIS([0,1,0,3,2,3]))
# 1
print(s.lengthOfLIS([7,7,7,7,7,7,7]))
# 3
print(s.lengthOfLIS([4,10,4,3,8,9]))