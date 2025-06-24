class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        s = set()
        for i in nums:
            if(i in s):
                s.remove(i)
            else:
                s.add(i)
        return s.pop()

s = Solution()


print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))
print(s.singleNumber([1]))
