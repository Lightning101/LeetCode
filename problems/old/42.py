class Solution:
    def trap(self, height) -> int:
        size = len(height)
        left,  right = [0] * size ,[0] * size
        
        left[0] = height[0]
        right[size-1] = height[size-1]
        for i in range(1,size):
            left[i] = max(height[i],left[i-1])
            right[size-i-1] = max(height[size-i - 1],right[size-i])
        
        ans = 0

        for i in range(size):
            ans+= min(left[i],right[i])-height[i]

        return ans



s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
