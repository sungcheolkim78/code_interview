from typing import List, Optional
from utils import TreeNode, build_tree, print_tree
from collections import defaultdict, deque


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        column_table = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                column_table[column].append(node.val)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [column_table[x] for x in sorted(column_table.keys())]


if __name__ == '__main__':
    solution = Solution()

    root = build_tree([3, 9, 20, None, None, 15, 7])
    print_tree(root)
    print(solution.verticalOrder(root))

    root = build_tree([3, 9, 8, 4, 0, 1, 7])
    print_tree(root)
    print(solution.verticalOrder(root))

    root = build_tree([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5])
    print_tree(root)
    print(solution.verticalOrder(root))
