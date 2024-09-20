from typing import Optional
import math
from utils import build_tree, print_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -float('inf')

        def gain_from_subtree(node: Optional[TreeNode]) -> int:
            nonlocal max_path

            if not node:
                return 0

            gain_from_left = max(gain_from_subtree(node.left), 0)
            gain_from_right = max(gain_from_subtree(node.right), 0)

            max_path = max(max_path, gain_from_left + gain_from_right + node.val)

            return max(gain_from_left + node.val, gain_from_right + node.val)

        gain_from_subtree(root)
        return max_path


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    root = build_tree([1, 2, 3])
    print_tree(root)
    print("")
    print(solution.maxPathSum(root))

    root = TreeNode(-10, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
    root = build_tree([-10, 9, 20, None, None, 15, 7])
    print_tree(root)
    print("")
    print(solution.maxPathSum(root))
