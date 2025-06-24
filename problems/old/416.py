class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # totalSum = sum(nums)
        # if totalSum % 2 != 0:
        #     return False
        # target = totalSum // 2
        target = 16
        dp = [[False for _ in range(target +1)]  for _ in range(len(nums ))]
        
        for i in range(len(nums)):
            prev = 0
            if(i>0 and nums[i]> nums[i-1]):
                dp[i] = dp[i-1][:]
                prev = nums[i-1]
            for j in range(prev,target+1):
                if(j == 0 or nums[i]==j):
                    dp[i][j] = True

        return True
        


s = Solution()

# True
print(s.canPartition([3,5,9,4,8]))

# False
# print(s.canPartition([1, 2, 3, 5]))


# print(s.canPartition([4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,12,12,12,12,12,12,12,12,16,16,16,16,16,16,16,16,20,20,20,20,20,20,20,20,24,24,24,24,24,24,24,24,28,28,28,28,28,28,28,28,32,32,32,32,32,32,32,32,36,36,36,36,36,36,36,36,40,40,40,40,40,40,40,40,44,44,44,44,44,44,44,44,48,48,48,48,48,48,48,48,52,52,52,52,52,52,52,52,56,56,56,56,56,56,56,56,60,60,60,60,60,60,60,60,64,64,64,64,64,64,64,64,68,68,68,68,68,68,68,68,72,72,72,72,72,72,72,72,76,76,76,76,76,76,76,76,80,80,80,80,80,80,80,80,84,84,84,84,84,84,84,84,88,88,88,88,88,88,88,88,92,92,92,92,92,92,92,92,96,96,96,96,96,96,96,96,97,99]))
