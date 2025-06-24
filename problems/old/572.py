# Definition for a binary tree node.
from LeetUtils import BuildBTree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dualTreeDFS(self, root1, root2):
        if root1 and root2 and root1.val == root2.val:
            left = root1.left == root2.left
            right = root1.right == root2.right

            if(not left):
                left =  self.dualTreeDFS(root1.left, root2.left)
            if(not right):
                right =  self.dualTreeDFS(root1.right, root2.right)

            return left and right
        return False

    def isSubtree(self, root, subRoot) -> bool:
        if root == None or root.val != subRoot.val:
            return False
        # if root.val != subRoot.val:
        #     return False
        return self.dualTreeDFS(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


s = Solution()

root= BuildBTree([3,4,5,1,2])
subRoot= BuildBTree([4,1,2])
print(s.isSubtree(root,subRoot))

# root = BuildBTree([3, 4, 5, 1, 2, None, None, None, None, 0])
# subRoot = BuildBTree([4, 1, 2])
# print(s.isSubtree(root, subRoot))

# root = BuildBTree([1,1])
# subRoot = BuildBTree([1])
# print(s.isSubtree(root, subRoot))
