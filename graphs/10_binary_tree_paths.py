from typing import List
from utils import TreeNode, build_tree, print_tree


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def construct_path(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += "->"
                    construct_path(root.left, path)
                    construct_path(root.right, path)

        paths = []
        construct_path(root, "")
        return paths

    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
        return paths


if __name__ == '__main__':
    root = build_tree([1, 2, 3, None, 5])
    print_tree(root)

    solution = Solution()
    paths = solution.binaryTreePaths2(root)
    print(paths)
