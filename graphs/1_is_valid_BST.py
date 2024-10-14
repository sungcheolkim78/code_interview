from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return validate(node.right, node.val, high) and validate(node.left, low, node.val)

        return validate(root)

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)

    def isValidBST3(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, -float('inf'), float('inf'))]
        while stack:
            node, low, high = stack.pop()

            if not node:
                continue

            if node.val <= low or node.val >= high:
                return False

            stack.append((node.right, node.val, high))
            stack.append((node.left, low, node.val))

        return True


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    print(sol.isValidBST2(root))

    root = TreeNode(5, TreeNode(1, None, None), TreeNode(4, TreeNode(3, None, None), TreeNode(6, None, None)))
    print(sol.isValidBST2(root))
