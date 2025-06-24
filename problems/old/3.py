class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = set()
        size = len(s)
        count = 0
        max_count = 0
        p1= p2 = 0
        
        while(p2<size):
            c = s[p2]
            if(c in mem):
                mem.remove(s[p1])
                count-=1
                p1+=1
            else:
                count+=1    
                p2+=1
                mem.add(c)
            
            if(count>max_count):
                max_count = count
        return max_count

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew")) 
print(s.lengthOfLongestSubstring("abcabcbb")) 
print(s.lengthOfLongestSubstring("bbbbb")) 
print(s.lengthOfLongestSubstring("abba")) 
print(s.lengthOfLongestSubstring("au")) 