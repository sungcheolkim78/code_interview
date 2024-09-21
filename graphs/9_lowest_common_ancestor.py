from typing import List
from utils import TreeNode, build_tree, print_tree


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse_tree(current_node: TreeNode) -> bool:
            if not current_node:
                return False

            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)

            mid = current_node == p or current_node == q

            if mid + left + right >= 2:
                self.ans = current_node

            return mid or left or right

        recurse_tree(root)
        return self.ans


if __name__ == '__main__':
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print_tree(root)
    solution = Solution()

    lca = solution.lowestCommonAncestor(root, root.left, root.left.right.right)
    print(lca.val)
