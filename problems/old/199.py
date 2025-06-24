from LeetUtils import BuildBTree
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#  BFS Solution
class Solution:

    def BFS(self,root,ans):
        st = deque()

        st.append(root)
        while(st):
            size = len(st)
            for i in range(size):
                node = st.popleft()
                if(i == size-1):
                    ans.append(node.val)

                if(node.left):
                    st.append(node.left)
                if(node.right):
                    st.append(node.right)
        return ans
    
    def rightSideView(self, root):
        if(root==None): return []
        return self.BFS(root,[])

# DFS Solution
class Solution:

    def DFS(self,root,lvl,ans):
        if(root == None):
            return
        if(ans.get(lvl) == None):
            ans[lvl]= root.val
        self.DFS(root.right,lvl+1,ans)
        self.DFS(root.left,lvl+1,ans)

    
    def rightSideView(self, root):
        if(root==None): return []
        ans = {}
        self.DFS(root,0,ans)
        return list(ans.values())

s = Solution()

# # [1,2,3,null,5,null,4]
# # [1,3,4]
# root = BuildBTree([1,2,3,None,5,None,4])
# print(s.rightSideView(root))

# # [1,2,3,4,null,null,null,5]
# # [1,3,4,5]
# root = BuildBTree([1,2,3,4,None,None,None,5])
# print(s.rightSideView(root))


# # [1,null,3]
# # [1,3]
# root = BuildBTree([1,None,3])
# print(s.rightSideView(root))

# # []
# # []
# root = BuildBTree([])
# print(s.rightSideView(root))


# [1,2,0]
# [1,0]
root = BuildBTree([1,2,0])
print(s.rightSideView(root))