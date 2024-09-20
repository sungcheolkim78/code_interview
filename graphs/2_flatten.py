from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flattenTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None

        if not node.left and not node.right:
            return node

        left_tail = self.flattenTree(node.left)
        right_tail = self.flattenTree(node.right)

        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        return right_tail if right_tail else left_tail

    def flatten(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenTree(root)

    def flatten2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        node = root
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                rightmost.right = node.right
                node.right = node.left
                node.left = None
            node = node.right


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)), TreeNode(5, TreeNode(6, None, None), None))
    sol.flatten2(root)
    print(root)
