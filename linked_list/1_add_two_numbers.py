from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def show_list(l: Optional[ListNode]):
    while l != None:
        print(l.val, end=" -> ")
        l = l.next
    print("")


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current_node = dummy_head
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            column_sum = l1_val + l2_val + carry
            carry = column_sum // 10

            new_node = ListNode(column_sum % 10)
            current_node.next = new_node
            current_node = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = ListNode(4, ListNode(5, ListNode(6)))
    show_list(l1)
    show_list(l2)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    show_list(result)
