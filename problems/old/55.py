# class Solution:
#     def canJump(self, nums: list[int]) -> bool:
#         return self.f(0,len(nums)-1,nums)

#     def f(self,c,n,nums):
#         if(c == n):
#             return True
#         elif(c>n):
#             return False
#         else:
#             subs = [False]
#             for i in range(1,nums[c] +1):
#                 subs.append(self.f(c+i,n,nums))
#             return any(subs)


# class Solution:
#     def canJump(self, nums: list[int]) -> bool:
#         size = len(nums)
#         reachTable = [False for _ in range(size)]
#         reachTable[0] = True

#         for i in range(size):
#             if reachTable[i]:
#                 for y in range(nums[i], 0, -1):
#                     if i + y < size:
#                         reachTable[i + y] = True
#                     else:
#                         return True
#         return reachTable[-1]



class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxReach = 0
        size = len(nums)
        for i in range(size):
            if(i<=maxReach):
                idxMax = i+nums[i]
                if(idxMax > maxReach):
                    maxReach = idxMax
            else:
                return False
        
        return maxReach>= size -1
        
s = Solution()

print(s.canJump([2,3,1,1,4]))
# print(s.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))

print(s.canJump([3, 2, 1, 0, 4]))
