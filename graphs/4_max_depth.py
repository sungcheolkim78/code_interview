from typing import Optional
import math
from utils import build_tree, print_tree, TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return 1 + max(left_depth, right_depth)


if __name__ == '__main__':
    solution = Solution()
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print_tree(root)
    print(solution.maxDepth(root))

    root = build_tree([1, None, 2])
    print_tree(root)
    print(solution.maxDepth(root))
