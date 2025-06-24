class Solution:
    def search(self,nums,key, last = False):
        left , right = 0 , len(nums)-1
        ans = -1
        while(left<=right):
            mid = (left + right)//2
            val = nums[mid]
            if( val == key):
                ans = mid
                if(last):
                    left = mid +1
                else:    
                    right = mid -1
            elif(val > key):
                right = mid -1
            else:
                left = mid+1
        return ans
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = self.search(nums,target)
        end = self.search(nums,target,True)
        return [start,end]

s = Solution()
print(s.searchRange([5,7,7,8,8,10],8))
print(s.searchRange([5,7,7,8,8,10],6))
print(s.searchRange([],0))
print(s.searchRange([1],1))
print(s.searchRange([1,1,2],1))