class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)
      
      
#Testing
tree = create_tree_from_list([3, 9, 20, None, None, 15, 7])
s = Solution()
print(s.maxDepth(tree))

def create_tree_from_list(tree_list) -> TreeNode:
    def rec(root=TreeNode(), index=0):
        if index < len(tree_list):
            if tree_list[index]:
                temp = TreeNode(tree_list[index])
                root = temp
            else:
                return None
            root.left = rec(root.left, 2 * index + 1)
            root.right = rec(root.right, 2 * index + 2)
        return root

    return rec()
