class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sizeA = len(a)
        sizeB = len(b)

        size= None
        workingStr = None
        if sizeA<sizeB:
            size = sizeB
            workingStr = [*b]
        else:
            size= sizeA
            workingStr= [*a]

        carry = 0
        for idx in range(-1,-size -1, -1):
            
            if(a[idx] =='1' and b[idx] == '1'):
                carry +=1
                workingStr[idx] = '0'
                if(carry == 2):
                    workingStr[idx] = '1'
                    carry-=1
            elif(a[idx] =='1' or b[idx] == '1'):
                workingStr = '1'
                if(carry):
                    workingStr[idx] = '0'
            else:
                if(carry== 1):
                    workingStr[idx]='1'
                    carry = 0
        if(carry):
            return "1".join(workingStr)
        return "".join(workingStr)

s = Solution()

print(s.addBinary("11","1"))
# print(s.addBinary("1010","1011"))