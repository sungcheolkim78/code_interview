from typing import List, Optional

class ListNode:
    def __init__(self, val: int, next=None, random=None):
        self.val = int(val)
        self.next = next
        self.random = random


def show_list(l: Optional[ListNode]):
    while l != None:
        print(f"{l.val}({l.random.val}) -> ", end="")
        l = l.next
    print("")


class Solution:
    def __init__(self):
        self.visited_hash = {}

    def copyRandomList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        if head in self.visited_hash:
            return self.visited_hash[head]

        node = ListNode(head.val, None, None)
        self.visited_hash[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


def create_random_node(l: List[List[int]]) -> Optional[ListNode]:
    node_list = [ListNode(0, None, None)] * len(l)
    print(node_list)

    for i in range(len(l) - 1):
        node_list[i].val = l[i][0]
        node_list[i].next = node_list[i + 1]
        if l[i][1] == None:
            node_list[i].random = None
        else:
            node_list[i].random = node_list[l[i][1]]

    print(node_list)
    return node_list[0]


if __name__ == "__main__":
    l1_list = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    l1 = create_random_node(l1_list)
    #show_list(l1)

    #solution = Solution()
    #result = solution.copyRandomList(l1)

    #show_list(result)
