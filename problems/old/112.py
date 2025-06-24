from LeetUtils import BuildBTree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root, target, nodeSum=0):
        left = False
        right = False
        if root.left:
            left = self.dfs(root.left, target, nodeSum + root.val)
        if root.right:
            right = self.dfs(root.right, target, nodeSum + root.val)
        
        if root.left == None and root.right == None:
            return (nodeSum + root.val) == target
        return left or right

    def hasPathSum(self, root, targetSum: int) -> bool:
        if root == None:
            return False
        return self.dfs(root, targetSum)


s = Solution()

root = BuildBTree([5,4,8,11,None,13,4,7,2,None,None,None,1])
print(s.hasPathSum(root,22))

# root = BuildBTree([1,2,3])
# print(s.hasPathSum(root,5))

# root = BuildBTree([1, 2])
# print(s.hasPathSum(root, 1))
