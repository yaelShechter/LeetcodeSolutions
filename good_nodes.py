class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def good_nodes(root: TreeNode) -> int:
    def rec(node=root, maximum=root.val):
        if not node:
            return 0
        if node.val < maximum:
            return rec(node.left, maximum) + rec(node.right, maximum)
        else:
            return 1 + rec(node.left, node.val) + rec(node.right, node.val)

    return rec()
  
  
#I wrote a function to build a tree from a list to make it easier to test the function 
#test case:
#[3,1,4,3,null,1,5]
def create_tree_from_list(tree_list) -> TreeNode:
    def rec(root, index):
        if index < len(tree_list):
            if tree_list[index]:
                temp = TreeNode(tree_list[index])
                root = temp
            else:
                return None
            root.left = rec(root.left, 2 * index + 1)
            root.right = rec(root.right, 2 * index + 2)
        return root

    return rec(TreeNode(), 0)

tree = create_tree_from_list([3, 1, 4, 3, None, 1, 5])
print(good_nodes(root))
