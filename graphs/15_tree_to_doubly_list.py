from typing import List, Optional
from utils import TreeNode, build_tree, print_tree, print_doubly_linked_list


class Solution:
    def treeToDoublyList(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            nonlocal last, first
            if node:
                helper(node.left)

                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node

                helper(node.right)

        if not root:
            return None

        first, last = None, None
        helper(root)

        last.right = first
        first.left = last

        return first


if __name__ == "__main__":
    root = build_tree([4, 2, 5, 1, 3])
    print_tree(root)
    first = Solution().treeToDoublyList(root)
    print_doubly_linked_list(first)

    root = build_tree([2, 1, 3])
    print_tree(root)
    first = Solution().treeToDoublyList(root)
    print_doubly_linked_list(first)

    root = build_tree([9, 5, 10, 2, 6, None, 11, 1, 4, None, 8])
    print_tree(root)
    first = Solution().treeToDoublyList(root)
    print_doubly_linked_list(first)
