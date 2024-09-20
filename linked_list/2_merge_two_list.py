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
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        prev = dummy_head

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 else l2

        return dummy_head.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = ListNode(2, ListNode(2, ListNode(5)))
    show_list(l1)
    show_list(l2)

    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)

    show_list(result)
