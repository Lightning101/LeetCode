# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TraveralOrder = ['left','current','right']

    def inorderTravel(self, root, ans):
        if(root and root.left):
            ans + self.inorderTravel(root.left, ans)
        if(root):
            ans.append(root.val)
        if(root and root.right):
            ans + self.inorderTravel(root.right, ans)
        return ans
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTravel(root,[])