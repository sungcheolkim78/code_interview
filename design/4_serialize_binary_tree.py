from graphs.utils import TreeNode, build_tree, print_tree
from typing import Optional


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


if __name__ == '__main__':
    root = build_tree([1, 2, 3, None, None, 4, 5])
    print_tree(root)
    codec = Codec()
    print(codec.serialize(root))
    new_root = codec.deserialize(codec.serialize(root))
    print_tree(new_root)
