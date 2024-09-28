from graphs.utils import TreeNode, build_tree, print_tree
from typing import Optional


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.nodes_sorted = []
        self.index = -1
        self._inorder(root)

    def _inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nodes_sorted)



if __name__ == '__main__':
    root = build_tree([7, 3, 15, None, None, 9, 20])
    print_tree(root)

    it = BSTIterator(root)
    instuctions = ["next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]

    for ins in instuctions:
        cmd = f"it.{ins}()"
        print(cmd, eval(cmd))
