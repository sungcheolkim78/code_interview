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
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        # find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge two sorted linked lists
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    show_list(head)

    Solution().reorderList(head)
    show_list(head)
