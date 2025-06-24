from LeetUtils import BuildBTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root):
        if(root == None):
            return (0,0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        depth = max(right[1],left[1])+1
        diameter = max(left[0],right[0], left[1]+right[1]+1)
        return  (diameter,depth )
        


    def diameterOfBinaryTree(self, root) -> int:
        if(not root.left and not root.right):
            return  0
        ans  = self.dfs(root)
        return ans[0] -1
        



root = BuildBTree([1,2,3,4,5])
# root = BuildBTree([1,2])
# root = BuildBTree([4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2])

s = Solution()

ans = s.diameterOfBinaryTree(root)
print(ans)