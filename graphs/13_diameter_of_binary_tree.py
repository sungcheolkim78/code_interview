from typing import Optional
from utils import TreeNode, build_tree, print_tree


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node) -> int:
            if not node:
                return 0
            nonlocal diameter

            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            diameter = max(diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter


if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, 5])
    print_tree(root)
    print(Solution().diameterOfBinaryTree(root))

    root = build_tree([1, 2, 3, 4, 5, None, 9, 6, 7, None, None, None, None, 10])
    print_tree(root)
    print(Solution().diameterOfBinaryTree(root))
