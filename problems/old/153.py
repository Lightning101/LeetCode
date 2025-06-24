class Solution:
    def findMin(self, nums: list[int]) -> int:
        size=len(nums)
        left , right = 0 ,size-1 
        ans = nums[0]
        while(left<=right):
            mid = (left + right)//2
            if(nums[mid] <= nums[size-1]):
                ans = nums[mid]
                right = mid -1
            else:
                left = mid+1
            
        return ans
    
s = Solution()

s.findMin([2,1])