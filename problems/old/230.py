from LeetUtils import BuildBTree
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,k,stack):
        if(root == None):
            return
        

        self.DFS(root.left,k,stack)

        size = len(stack)

        if(size < k or stack[-1] > root.val):
            stack.append(root.val)
            size+=1
        else:
            return

        if(size > k ):
            stack.popleft()
        
        
        self.DFS(root.right,k,stack)




    def kthSmallest(self, root, k: int) -> int:
        st = deque()
        self.DFS(root,k,st)
        return st[-1]
    

s = Solution()

root = BuildBTree([3,1,4,None,2])
print(s.kthSmallest(root,1))

# root = BuildBTree([5,3,6,2,4,None,None,1])
# print(s.kthSmallest(root,3))

# root = BuildBTree([1,None,2])
# print(s.kthSmallest(root,2))

        
        