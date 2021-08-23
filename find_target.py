def find_target(root, k):
    nodes_values = {}

    def rec(node):
        if not node:
            return False
        if node.val in nodes_values:
            return True
        nodes_values[k - node.val] = True
        return rec(node.left) or rec(node.right)

    return rec(root)

  
#Testing:
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
  
  
l1 = create_tree_from_list([5, 3, 6, 2, 4, None, 7])
assert find_target(l1, 9)
assert not find_target(l1, 15)
