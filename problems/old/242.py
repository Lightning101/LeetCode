class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0]*26
        i = 0
        while (p1:=s[i:i+1]) and (p2:=t[i:i+1]):
            alpha[ord(p1[0])- 97] += 1
            alpha[ord(p2[0])- 97] -= 1
            i+=1
        
        
        return not s[i:i+1] and not t[i:i+1] and   not any(alpha)

s = Solution()

# print(s.isAnagram("ggii","eekk"))
# print(s.isAnagram("anagram","nagaram"))
print(s.isAnagram("a","ab"))