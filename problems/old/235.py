from LeetUtils import BuildBTree
from collections import deque


def binarySearch(root, key):
    node = root
    while node:
        if key == node.val:
            return node
        elif key < node.val:
            node = node.left
        else:
            node = node.right
    return None


class Solution:
    def stepBinarySearch(self,root, key):
        node = root
        if key == node:
            return (True, node)
        elif key.val < node.val:
            node = node.left
        else:
            node = node.right
        return (False , node)

    def lowestCommonAncestor(self, root, p, q):
        ans = root
        while(True):
            pPath = self.stepBinarySearch(ans,p)
            qPath = self.stepBinarySearch(ans,q)
            
            if(pPath[0] or qPath[0]):
                ans = pPath[1] if pPath[0] else qPath[1]
                break
            if(pPath[1] == qPath[1]):
                ans = pPath[1]
            else:
                break
        return ans


s = Solution()


# [6,2,8,0,4,7,9,null,null,3,5]
root = BuildBTree([6,2,8,0,4,7,9,None,None,3,5])
print(s.lowestCommonAncestor(root,binarySearch(root, 2),binarySearch(root, 8)).val)

# [6,2,8,0,4,7,9,null,null,3,5]
root = BuildBTree([6,2,8,0,4,7,9,None,None,3,5])
print(s.lowestCommonAncestor(root,binarySearch(root, 2),binarySearch(root, 4)).val)

# [2,1]
root = BuildBTree([2,1])
print(s.lowestCommonAncestor(root,binarySearch(root, 2),binarySearch(root, 1)).val)


# [3,1,4,null,2] 3
root = BuildBTree([3, 1, 4, None, 2])
# p = 2, q = 4
print(s.lowestCommonAncestor(root, binarySearch(root, 2), binarySearch(root, 4)).val)
