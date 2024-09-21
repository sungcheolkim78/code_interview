from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while i < len(values):
        curr = queue.popleft()

        if i < len(values):
            if values[i]:
                curr.left = TreeNode(values[i])
                queue.append(curr.left)
            i += 1

        if i < len(values):
            if values[i]:
                curr.right = TreeNode(values[i])
                queue.append(curr.right)
            i += 1

    return root

def print_tree(root: Optional[TreeNode]):
    if not root:
        return

    print("Tree:", end=" ")
    q = deque([root])
    order = 0
    while q:
        curr = q.popleft()
        print(f"{curr.val}({order})", end=" ")

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
        if curr.left or curr.right:
            order += 1
    print("")


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


if __name__ == '__main__':
    root = build_tree([1, 2, 3])
    print_tree(root)

    root = build_tree([3, 9, 20, None, None, 15, 7])
    print_tree(root)
