from LeetUtils import BuildBTree
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root, targetSum: int,ans = None, comb= None) -> bool:
        if(root == None):
            return
        if(comb == None):
            comb = deque()
        if(ans == None):
            ans = []
        
        targetSum -= root.val
        comb.append(root.val)

        if root.left == None and root.right == None:
            if(targetSum == 0):
                ans.append(list(comb))
        
        self.hasPathSum(root.left, targetSum,ans,comb)
        self.hasPathSum(root.right, targetSum,ans,comb)
        comb.pop()
        return  ans


    def pathSum(self, root, targetSum: int):
        return self.hasPathSum(root,targetSum)
        


s = Solution()


root = BuildBTree([5,4,8,11,None,13,4,7,2,None,None,5,1])
ans = s.pathSum(root,22)

# root = BuildBTree([1,2,3])
# ans = s.pathSum(root,5)

# root = BuildBTree([1,2])
# ans = s.pathSum(root,0)



print(ans)