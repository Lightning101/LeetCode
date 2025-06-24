from collections import deque
class Solution:
    def nextGreaterElements(self, nums) :
        size = len(nums)
        st = deque()
        st.append(0)

        ans = [-1] * size
        for i in range(1,size):
            while(len(st)>0 and nums[st[-1]] < nums[i]):
                ans[st.pop()] = nums[i]
            st.append(i)
        
        
        for i in range(0,size):
            while(len(st)>0 and nums[st[-1]] < nums[i]):
                ans[st.pop()] = nums[i]
        
        return ans

        
        
    
s = Solution()
print(s.nextGreaterElements([1,2,1])) 