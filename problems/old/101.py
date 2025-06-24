# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.IsSym(root.left,root.right)

    def IsSym(self,n1,n2):
        if(n1 == None and n2 == None):
            return True
        elif(not n1 or not n1):
            return False
        elif(n1.val != n2.val):
            return False

        return self.IsSym(n1.left,n2.right) and self.IsSym(n1.right,n2.left)
        