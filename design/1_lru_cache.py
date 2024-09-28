from typing import Optional
from collections import OrderedDict

class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.next: Optional[ListNode] = None
        self.prev: Optional[ListNode] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            self.show_cache()
            return -1
        node = self.dic[key]
        self.remove(node)
        self.add(node)

        self.show_cache()
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_remove = self.head.next
            self.remove(node_to_remove)
            del self.dic[node_to_remove.key]

        self.show_cache()

    def add(self, node: ListNode):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def show_cache(self):
        msg = []
        curr = self.head.next
        while curr != self.tail:
            msg.append(f"{curr.key}={curr.val}")
            curr = curr.next
        print('cache is {' + ','.join(msg) + '}')


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)

        self.show_cache()
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)

        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)

        self.show_cache()

    def show_cache(self):
        print('cache is {' + ','.join([f"{k}={v}" for k, v in self.dic.items()]) + '}')


if __name__ == '__main__':
    instructions = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    lru_cache = LRUCache2(values[0][0])
    for ins, val in zip(instructions[1:], values[1:]):
        if len(val) == 1:
            cmd = f"lru_cache.{ins}({val[0]})"
        else:
            cmd = f"lru_cache.{ins}({val[0]}, {val[1]})"
        print(cmd)
        eval(cmd)
