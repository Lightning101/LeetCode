from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1 , max(piles)
        ans = 1
        while(left<=right):
            mid = (left + right) // 2
            time_taken = sum([ ceil(n / mid)  for n in piles])
            if(time_taken>h):
                left = mid+1
            else:
                ans = mid
                right = mid -1
        return ans
        
s = Solution()

# print(s.minEatingSpeed([3,6,7,11],8))
# print(s.minEatingSpeed([30,11,23,4,20],5))
# print(s.minEatingSpeed([30,11,23,4,20],6))
# print(s.minEatingSpeed([2,2],2))
print(s.minEatingSpeed([312884470],312884469))


        