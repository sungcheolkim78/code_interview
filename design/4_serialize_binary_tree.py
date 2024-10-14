from graphs.utils import TreeNode, build_tree, print_tree
from typing import Optional
from collections import deque


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def r_serialize(root, string):
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = r_serialize(root.left, string)
                string = r_serialize(root.right, string)
            return string
        return r_serialize(root, '')

    def deserialize(self, data: str) -> Optional[TreeNode]:
        def r_deserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(int(l[0]))
            l.pop(0)
            root.left = r_deserialize(l)
            root.right = r_deserialize(l)
            return root

        data_list = data.split(',')
        root = r_deserialize(data_list)
        return root

    def serialize2(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''

        data = []

        # bfs
        q = deque([root])
        while q:
            if all([n is None for n in q]):
                break
            node = q.popleft()
            if node is None:
                data.append('null')
                continue
            else:
                data.append(node.val)

            q.append(node.left)
            q.append(node.right)

        return ','.join([str(d) for d in data])

    def deserialize2(self, data: str) -> Optional[TreeNode]:
        if data == '':
            return None

        data_list = data.split(',')
        index = 1

        # bfs
        root = TreeNode(int(data_list[0]))
        q = deque([root])
        while q:
            node = q.popleft()
            if index < len(data_list):
                if data_list[index] != 'null':
                    node.left = TreeNode(int(data_list[index]))
                    q.append(node.left)
                index += 1
            if index < len(data_list):
                if data_list[index] != 'null':
                    node.right = TreeNode(int(data_list[index]))
                    q.append(node.right)
                index += 1

        return root


if __name__ == '__main__':
    root = build_tree([1, 2, 3, None, None, 4, 5])
    print_tree(root)
    codec = Codec()
    print(codec.serialize2(root))
    new_root = codec.deserialize2(codec.serialize2(root))
    print_tree(new_root)
