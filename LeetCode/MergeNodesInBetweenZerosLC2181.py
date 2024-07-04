from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = head
    current = head.next

    while current:
        if current.val == 0 and not current.next:
            prev.next = None
            prev.val += current.val
        elif current.val == 0:
            prev.next = current
            prev = prev.next
        else:
            prev.val += current.val
        current = current.next

    return head