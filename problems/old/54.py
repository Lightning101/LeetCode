class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        xSize = len(matrix[0])
        ySize = len(matrix)
        top,left,bot,right = 0,0,ySize-1,xSize-1

        direction = 0 

        ans=[matrix[0][0]]
        y,x=0,1
        chngDir = lambda d :(d +1) % 4

        while(top <= bot and left <= right):
            #  Left to Right
            if direction == 0:
                while(x<=right):
                    ans.append(matrix[y][x])
                    x+=1
                x-=1
                y+=1
                top+=1
            #  Top to Bottom
            elif direction == 1:
                while(y<=bot):
                    ans.append(matrix[y][x])
                    y+=1
                y-=1
                x-=1
                right -=1
            # Right to left 
            elif direction == 2:
                while(x>= left):
                    ans.append(matrix[y][x])
                    x-=1
                x+=1
                y-=1
                bot-=1
            # Bottom to top
            else:
                while(y>=top):
                    ans.append(matrix[y][x])
                    y-=1
                y+=1
                x+=1
                left+=1
            direction  = chngDir(direction)
        return ans
    
s = Solution()

print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))