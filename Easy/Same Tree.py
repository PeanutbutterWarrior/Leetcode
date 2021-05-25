from leetcode_builtins import TreeNode

def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    
    try:
        return isSameTree(p.left, q.left) and p.val == q.val and isSameTree(p.right, q.right)
    except AttributeError:
        return False
