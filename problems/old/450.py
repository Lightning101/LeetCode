from LeetUtils import BuildBTree, BTreePrint


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def BS(self, root, prev, key):
        if root.val == key:
            return (root, prev)
        elif key > root.val:
            if root.right:
                return self.BS(root.right, root, key)
        elif key < root.val:
            if root.left:
                return self.BS(root.left, root, key)
        return None

    def deleteNode(self, root, key: int):
        if not root:
            return root

        result = self.BS(root, None, key)

        if not result:
            return root

        deleteNode = result[0]
        parent = result[1]

        if not (deleteNode.left or deleteNode.right):
            if parent:
                if parent.left == deleteNode:
                    parent.left = None
                else:
                    parent.right = None
            else:
                return None
        elif deleteNode.left == None or deleteNode.right == None:
            if deleteNode.left:
                if parent:
                    if parent.left == deleteNode:
                        parent.left = deleteNode.left
                    else:
                        parent.right = deleteNode.left
                else:
                    return deleteNode.left
            else:
                if parent:
                    if parent.right == deleteNode:
                        parent.right = deleteNode.right
                    else:
                        parent.left = deleteNode.right
                else:
                    return deleteNode.right
        else:

            def dfs(node, parent):
                if node.left:
                    return dfs(node.left, node)
                return node,parent

            (inNode, inParent) = dfs(deleteNode.right, deleteNode)

            if inParent.left == inNode:
                inParent.left = inNode.right
            else:
                inParent.right = inNode.right

            if parent:
                if parent.left == deleteNode:
                    parent.left = inNode
                else:
                    parent.right = inNode

            inNode.left = deleteNode.left
            inNode.right = deleteNode.right
            if deleteNode == root:
                return inNode
        return root


s = Solution()

# 3
# root = BuildBTree([5, 3, 6, 2, 4, None, 7])
# 5
# root = BuildBTree([5, 3, 6, 2, 4, None, 7])

# 1
# root = BuildBTree([3,1,2,None,4])


root = BuildBTree([2,0,33,None,1,25,40,None,None,11,31,34,45,10,18,29,32,None,36,43,46,4,None,12,24,26,30,None,None,35,39,42,44,None,48,3,9,None,14,22,None,None,27,None,None,None,None,38,None,41,None,None,None,47,49,None,None,5,None,13,15,21,23,None,28,37,None,None,None,None,None,None,None,None,8,None,None,None,17,19,None,None,None,None,None,None,None,7,None,16,None,None,20,6])


BTreePrint(s.deleteNode(root, 33))
print()
