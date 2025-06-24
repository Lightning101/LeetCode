from collections import deque
class Solution:
    def rob(self, nums: list[int]) -> int:
        size = len(nums)
        if(size == 1):
            return nums[0]
        dp = deque([0]*3)

        for i in range(len(nums)):
            ans1 = dp[1]
            ans2=dp[0]
            dp.append(nums[i] + max(ans1,ans2))
            dp.popleft()
        return max(dp[-1],dp[-2])
    
s = Solution()

print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))