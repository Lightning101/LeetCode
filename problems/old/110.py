from LeetUtils import  BuildBTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def height(self,root,lvl = 0):
        if(root == None):
            return lvl
        
        left = self.height(root.left, lvl)

        if(left == -1):
            return -1

        right = self.height(root.right, lvl)

        if(right == -1):
            return -1
 
        if(abs(left-right) > 1):
            return -1

        return max(left ,right) +1

    def isBalanced(self, root: list[TreeNode]) -> bool:
        if(root == None):
            return True
        
        return self.height(root) != -1
    

s = Solution()

root = BuildBTree([3,9,20,None,None,15,7])
print(s.isBalanced(root))

root = BuildBTree([1,2,2,3,3,None,None,4,4])
print(s.isBalanced(root))

root = BuildBTree([])
print(s.isBalanced(root))

root = BuildBTree([1,2,2,3,None,None,3,4,None,None,4])
print(s.isBalanced(root))