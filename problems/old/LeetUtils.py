import math
import collections


# Leet Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def CreateBSTFromValues(values: list) -> TreeNode | None:
    """
    CreateBSTFromValues Creates BTree from value list
    !Works only for order maintained value list

    :param values: flat list of values which can contain None
    :return: Root tree node or none
    """
    numOfNodes = len(values)
    if numOfNodes == 0:
        return None
    # Create nodes for all does not work well with null
    nodes = [TreeNode(i) if (i != None) else None for i in values]

    root = nodes[0]
    # Calc the height of the tree
    height = math.floor(math.log(numOfNodes, 2)) + 1

    for lvl in range(1, height):
        startOfLvlIndx = ((lvl - 1) * 2) + 1
        endOfLvlIndx = (lvl + 1) * 2
        for childIndx in range(startOfLvlIndx, endOfLvlIndx + 1):
            #  Reached end of children for lvl
            if(childIndx >= numOfNodes):
                break 
            # Found None Value dont process
            if nodes[childIndx] == None:
                continue
            # Calc Parent
            parent =childIndx +  1 if(childIndx % 2)else 2
            parent = parent //2 - 1
            # Even left and odd right
            if childIndx % 2 == 0:
                nodes[parent].right = nodes[childIndx]
            else:
                nodes[parent].left = nodes[childIndx]
    return root

# Stack overflow https://stackoverflow.com/a/78269172
def BuildBTree(nodes: list, includeNone = False) -> TreeNode:
    n = len(nodes)

    if n == 0:
        return None

    parentStack = collections.deque()
    root = TreeNode(nodes[0])
    curParent = root

    for i in range(1, n):
        if i % 2 == 1:
            if nodes[i] is not None or includeNone:
                curParent.left = TreeNode(nodes[i])
                parentStack.append(curParent.left)
        else:
            if nodes[i] is not None or includeNone:
                curParent.right = TreeNode(nodes[i])
                parentStack.append(curParent.right)

            curParent = parentStack.popleft()

    return root

def BTreePrint(root: TreeNode):
    parentStack = collections.deque()
    parentStack.append(root)
    lvl = 0
    while(parentStack):

        print(f"Level: {lvl}")
        print("[",end="")
        for _ in range(len(parentStack)):
            node = parentStack.popleft()
            print(f"{node.val},",end="")
            if(node.val == None):
                continue
            if(node.left):
                parentStack.append(node.left)
            else:
                parentStack.append(TreeNode(None))
            if(node.right):
                parentStack.append(node.right)
            else:
                parentStack.append(TreeNode(None))
        print("]")
        lvl+=1
   


    