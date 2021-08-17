class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    def rec(node=root, maximum=root.val):
        if not node:
            return 0
        if node.val < maximum:
            return rec(node.left, maximum) + rec(node.right, maximum)
        else:
            return 1 + rec(node.left, node.val) + rec(node.right, node.val)

    return rec()
  
  
#test case:
#[3,1,4,3,null,1,5]
son3 = TreeNode(3)
son1 = TreeNode(1, son3)
son11 = TreeNode(1)
son5 = TreeNode(5)
son4 = TreeNode(4, son11, son5)
root = TreeNode(3, son1, son4)
print(goodNodes(root))
