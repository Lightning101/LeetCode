class Solution:
    
    def getCoinsNeeded(self,amount,coins,memo):
        if(amount<=0):
            return 0
        else:
            if(amount in memo):
                return memo[amount]
            ans = -1
            for j in coins:
                if(j<=amount):
                    val = self.getCoinsNeeded(amount-j,coins,memo)
                    if(val !=-1 and (ans ==-1 or val+1 < ans)):
                        ans = val +1

            memo[amount] = ans
            return ans
    
    def coinChange(self, coins: list[int], amount: int) -> int:
        return self.getCoinsNeeded(amount,coins,{})
        
s = Solution()

# 3
# print(s.coinChange([1,2,5],11))

# -1
# print(s.coinChange([2], 3))

# 0
# print(s.coinChange([1], 0))

# 2
# print(s.coinChange([3,5,7], 8))

# 20
print(s.coinChange([186,419,83,408], 6249))