from LeetUtils import BuildBTree
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self,root,currentMax= float("-inf")):
        if(root==None):
            return 0
        
        goodNode = 0
        if(currentMax<= root.val):
            currentMax = root.val
            goodNode = 1
        
        left = self.DFS(root.left,currentMax)
        right = self.DFS(root.right,currentMax)

        return left + right + goodNode

    def goodNodes(self, root) -> int:
        return self.DFS(root)


s = Solution()

root = BuildBTree([3,1,4,3,None,1,5])
print(s.goodNodes(root))

# root = BuildBTree([3,3,None,4,2])
# print(s.goodNodes(root))

# root = BuildBTree([1])
# print(s.goodNodes(root))

def Non_Recursive_dfs(root):
    stack = deque()
    stack.append(root)
    path = []
    while stack:
        s = stack.pop()  
        path.append(str(s.val))      
        
        if(s.right):
            stack.append(s.right)
        if(s.left):
            stack.append(s.left)
    
    return " ".join(path)

print(Non_Recursive_dfs(root))