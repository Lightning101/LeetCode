from LeetUtils import BuildBTree

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def levelOrderTraversal(self,root,x,y):
        if(root == None):
            return False
        
        q  =deque()
        q.append(root)

        while(q):
            xParent = None
            yParent = None
            for _ in range(len(q)):
                node = q.popleft()

                def processSubNode(subNode, hashVal):
                    if(subNode):
                        if(subNode.val == x):
                            nonlocal xParent
                            xParent = hashVal
                        if(subNode.val == y):
                            nonlocal yParent
                            yParent = hashVal

                def processNode(mainNode):
                    q.append(mainNode)
                    hashVal = id(mainNode)
                    processSubNode(mainNode.left,hashVal)
                    processSubNode(mainNode.right,hashVal)

                if(node.left):
                    processNode(node.left)

                if(node.right):
                    processNode(node.right)

                if(xParent and yParent and xParent != yParent):
                    return True
        return False

    def isCousins(self, root, x: int, y: int) -> bool:
        return self.levelOrderTraversal(root,x,y)
        

s = Solution()

root = BuildBTree([1,2,3,4])
print(s.isCousins(root,4,3))

# # [1,2,3,null,4,null,5]
# root = BuildBTree([1,2,3,None,4,None,5])
# print(s.isCousins(root,5,4))

# # [1,2,3,null,4]
# root = BuildBTree([1,2,3,None,4])
# print(s.isCousins(root,2,3))

# # [1,3,2,null,null,7,4,null,null,5,6,null,8,null,9]
# root = BuildBTree([1,3,2,None,None,7,4,None,None,5,6,None,8,None,9])
# print(s.isCousins(root,8,9))

# [1,2,4,3,19,10,5,15,8,null,null,13,14,null,6,null,17,null,null,null,null,18,null,7,11,null,null,null,null,null,9,16,12,null,null,20]
# root = BuildBTree([1,2,4,3,19,10,5,15,8,None,None,13,14,None,6,None,17,None,None,None,None,18,None,7,11,None,None,None,None,None,9,16,12,None,None,20])
# print(s.isCousins(root,11,17))

# [1,2,3,null,null,4,5]
# root = BuildBTree([1,2,3,None,None,4,5])
# print(s.isCousins(root,4,5))