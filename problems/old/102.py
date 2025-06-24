from LeetUtils import BuildBTree
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if(root == None):
            return []

        ans = []
        parentQueue  = deque()
        parentQueue.append(root)

        childrenQueue = deque()

        while(parentQueue or childrenQueue):
            level = []
            while(parentQueue):
                parent = parentQueue.popleft()
                level.append(parent.val)
                if(parent.left):
                    childrenQueue.append(parent.left)
                if(parent.right):
                    childrenQueue.append(parent.right)
            ans.append(level)
            parentQueue = childrenQueue
            childrenQueue = deque()
        
        return ans




s = Solution()

root = BuildBTree([3,9,20,None,None,15,7])
# root = BuildBTree([])
# root = BuildBTree([1])

print(s.levelOrder(root))
        