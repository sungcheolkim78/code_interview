from typing import Optional
from utils import Node


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val, [])
        self.visited[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node


if __name__ == '__main__':
    solution = Solution()

    node = Node(1, [Node(2), Node(3)])
    print(solution.cloneGraph(node))

    node = Node(1, [Node(2, [Node(4), Node(5)]), Node(3)])
    print(solution.cloneGraph(node))

    node = Node(1, [Node(2, [Node(4), Node(5)]), Node(3, [Node(6), Node(7)])])
    print(solution.cloneGraph(node))
