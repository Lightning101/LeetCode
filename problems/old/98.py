from LeetUtils import BuildBTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self,root, minV = float('-inf'), maxV = float('inf')) -> bool:
        
        left = True
        right = True

        if(root.val <= minV or root.val >= maxV) :
            return False
        
        if(root.left):
            left = self.DFS(root.left,minV,root.val)
        if(root.right):
            right = self.DFS(root.right,root.val, maxV)

        return left and right 

    def isValidBST(self, root) -> bool:
        return self.DFS(root)
    


s = Solution()

# root = BuildBTree([2,1,3])
# print(s.isValidBST(root))

# root = BuildBTree([5,1,4,None,None,3,6])
# print(s.isValidBST(root))

# root = BuildBTree([5,4,6,None,None,3,7])
# print(s.isValidBST(root))

root = BuildBTree([0,None,-1])
print(s.isValidBST(root))
