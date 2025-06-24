# Definition for a binary tree node.
from LeetUtils import BTreePrint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def divideTree(self,left,right,preorder,inorderMap):
        if(left>right):
            return None
        root = TreeNode(preorder[self.preIdx])

        rootIdx = inorderMap[root.val]
        self.preIdx +=1

        root.left = self.divideTree(left, rootIdx-1,preorder,inorderMap ) 
        root.right = self.divideTree(rootIdx+1, right,preorder,inorderMap ) 

        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> list[TreeNode] | None:
        size =len(inorder)
        inorderMap = { inorder[i]   : i for i in range(size)}
        self.preIdx = 0
        return self.divideTree(0,size-1,preorder,inorderMap)




s = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

BTreePrint(s.buildTree(preorder,inorder))



# preorder = [-1]
# inorder = [-1]

# print(s.buildTree(preorder,inorder))