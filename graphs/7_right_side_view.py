from typing import Optional, List
from utils import build_tree, print_tree, TreeNode
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        next_level = deque([root])
        right_side = []

        while next_level:
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            right_side.append(node.val)

        return right_side

    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        right_side = []
        while q:
            level_length = len(q)

            for i in range(level_length):
                node = q.popleft()

                if i == level_length - 1:
                    right_side.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return right_side


if __name__ == '__main__':
    solution = Solution()
    root = build_tree([1, 2, 3, None, 5, None, 4])
    print_tree(root)
    print(solution.rightSideView2(root))

    root = build_tree([1, None, 3])
    print_tree(root)
    print(solution.rightSideView2(root))

    root = build_tree([])
    print_tree(root)
    print(solution.rightSideView2(root))
