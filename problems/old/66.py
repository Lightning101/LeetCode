class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        size = len(digits)

        for idx in range(size -1, -1, -1):
            digits[idx] +=1
            if( digits[idx] == 10 ):
                digits[idx] = 0
            else:
                return digits


        return [1] + digits

s = Solution()

# print(s.plusOne([1, 2, 3]))
# print(s.plusOne([4,3,2,1]))
print(s.plusOne([9]))
