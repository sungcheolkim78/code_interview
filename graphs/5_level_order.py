from typing import List, Optional
from collections import deque

from utils import build_tree, print_tree, TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node: TreeNode, level: int) -> None:
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)

            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root])
        while queue:
            levels.append([])
            level_length = len(queue)

            for _ in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return levels


if __name__ == '__main__':
    solution = Solution()

    root = build_tree([3, 9, 20, None, None, 15, 7])
    print_tree(root)
    print(solution.levelOrder2(root))

    root = build_tree([1])
    print_tree(root)
    print(solution.levelOrder2(root))

    root = build_tree([])
    print_tree(root)
    print(solution.levelOrder2(root))
