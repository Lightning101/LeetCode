from collections import deque
class Solution:
    def merge(self, intervals):
        size = len(intervals)
        ans = []

        intervals.sort(key= lambda x: (x[0],x[1]))
        ans.append(intervals[0])
        for i in range(1,size) :
            e1= intervals[i][0]
            e2= intervals[i][1]
            
            if(e1<=ans[-1][0] and ans[-1][1] <= e2):
                ans[-1][0] = e1
                ans[-1][1] = e2
            elif(e1<=ans[-1][0]):
                ans[-1][0] = e1
            elif(ans[-1][1] <= e2 and e1<ans[-1][1]):
                ans[-1][1] = e2
            elif(e1>ans[-1][1]):
                ans.append([e1,e2])


        return ans
    
s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]])) 