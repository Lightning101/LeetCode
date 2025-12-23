# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildNode(self, left, right, postorder, indexMap):
        if left > right:
            return None

        val = postorder.pop()

        root = TreeNode(val)

        index = indexMap[val]

        root.right = self.buildNode(index + 1, right, postorder, indexMap)
        root.left = self.buildNode(left, index - 1, postorder, indexMap)
        return root

    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:

        indexMap = {inorder[i]: i for i in range(len(inorder))}
        return self.buildNode(0, len(inorder) - 1, postorder, indexMap)


s = Solution()


# print(s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
print(s.buildTree([3, 2, 1], [3, 2, 1]))
