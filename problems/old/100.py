from LeetUtils import BuildBTree




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrderTraversal(self,root1,root2):
        if(root1 == root2):
            return True
        
        if((root1== None or root2 == None) or (root1.val != root2.val)):
            return False

        return True and self.preOrderTraversal(root1.left,root2.left) and self.preOrderTraversal(root1.right, root2.right) 


    def isSameTree(self, p, q) -> bool:
        return self.preOrderTraversal(p,q)
        

s = Solution()

root1 = BuildBTree([1,2,3])
root2 = BuildBTree([1,2,3])
print(s.isSameTree(root1,root2))

# [1,2]
# [1,null,2]
root1 = BuildBTree([1,2])
root2 = BuildBTree([1,None,2])
print(s.isSameTree(root1,root2))

root1 = BuildBTree([1,2,1])
root2 = BuildBTree([1,1,2])
print(s.isSameTree(root1,root2))