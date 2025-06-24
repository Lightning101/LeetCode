class Solution:

    def isAlpNum(self,c):
        return  (64 < c and c < 91) or (47 < c and c < 58)
    def isPalindrome(self, s: str) -> bool:
        
        size = len(s)
        l,r= 0,size-1
        while(r>l):
            left = ord(s[l].upper())
            right = ord(s[r].upper())
            
            isAlpNumL = self.isAlpNum(left)
            isAlpNumR = self.isAlpNum(right)

            if(isAlpNumL and isAlpNumR):
                if(left == right):
                    l+=1
                    r-=1
                else:
                    return False
            elif(not isAlpNumL):
                l +=1
            else:
                r-=1
        
        return True


s = Solution()

# print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome("race a car"))
# print(s.isPalindrome(" "))
print(s.isPalindrome("0P"))