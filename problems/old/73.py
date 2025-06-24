class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is1Col0, is1Row0 = False, False
        ySize = len(matrix)
        xSize = len(matrix[0])
        for i in range(xSize):
            if(matrix[0][i] == 0):
                is1Row0 = True
                break
        for i in range(ySize):
            if(matrix[i][0] == 0):
                is1Col0 = True
                break
        
        for y in range(ySize):
            for  x in range(xSize):
                if(matrix[y][x] ==0):
                    matrix[y][0] = 0
                    matrix[0][x] = 0
        for y in range(1,ySize):  
            for x in range(1,xSize):  
                if(matrix[0][x] == 0 or matrix[y][0]==0):
                    matrix[y][x]= 0
                print()    
                print()    
                for y in range(ySize):
                    print(matrix[y])
     
        
        if(is1Col0):
            for y in range(ySize):
                matrix[y][0]=0
        if(is1Row0):
            matrix[0] = [0] * xSize
        

s = Solution()

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix = [[1,1,1],[1,0,1],[1,1,1]]

ySize = len(matrix)
xSize = len(matrix[0])


# print("====== Original ======")
# for y in range(ySize):
#     print('[',matrix[y],']')



s.setZeroes(matrix)

print("====== Modified ======")
for y in range(ySize):
    print('[',matrix[y],']')
