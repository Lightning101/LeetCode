from LeetUtils import BuildBTree
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxLevelSum(self, root) -> int:
        ans = (root.val, 1)

        q = deque([root])
        level = 0
        while q:
            levelSum = 0
            level += 1
            for i in range(len(q)):
                node = q.popleft()
                levelSum += node.val
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

            if levelSum > ans[0]:
                ans = (levelSum, level)

        return ans[1]


s = Solution()
root = BuildBTree([989, None, 10250, 98693, -89388, None, None, None, -32127])


print(s.maxLevelSum(root))
