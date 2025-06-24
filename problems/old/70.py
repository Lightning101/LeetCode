#  Top down with memo
# class Solution:
#     def climbStairs(self, n: int, memo=None) -> int:
#         if(memo== None):
#             memo = {}
#         if(n in memo):
#             return memo[n]
#         if(n <=2):
#             return n
#         memo[n] = self.climbStairs(n-1,memo) + self.climbStairs(n-2,memo)
#         return  memo[n]
    
#  Bottom up without memo
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         pass

#     def f(self,i,n):
#         if(i>n):
#             return 0
#         elif(i ==n):
#             return 1
#         else:
#             return self.f(i+1,n) + self.f(i+2,n)
        

class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<= 3):
            return n
        prev1 = 3
        prev2 = 2

        for _ in range(3,n):
            curr = prev1 + prev2
            prev2 = prev1 
            prev1 = curr

        return prev1

        

s = Solution()

# print(s.climbStairs(5))
print(s.climbStairs(6))