from leetcode_builtins import TreeNode

def inorder_tree_traversal(self, root: TreeNode) -> List[int]:
    if root is None:
        return []
    
    output = []
    output += inorderTraversal(root.left)
    output.append(root.val)
    output += inorderTraversal(root.right)
    
    return output
