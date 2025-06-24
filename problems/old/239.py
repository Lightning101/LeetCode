from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        ans = []
        size = len(nums)
        for i in range(size):

            while(dq and dq[0] < i - k+1):
                dq.popleft()
            while(dq and nums[dq[-1]] < nums[i]):
                dq.pop()
            
            
            dq.append(i)
            if(i >= k -1):
                ans.append(nums[dq[0]])
        return ans

        
    



s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)) 
# print(s.maxSlidingWindow([1,-1],1)) 