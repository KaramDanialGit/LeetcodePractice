from typing import Optional, List

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.ListNode = None

def insertGreatestCommonDivisors(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return []

    gcds = []
    prev = head.val
    current = head.next

    if not current:
        return head

    while current:
        gcds.append(ListNode(gcd(prev, current.val)))
        prev = current.val
        current = current.next

    index = 0
    current = head
    nextNode = current.next

    while current:
        if index >= len(gcds):
            break
        current.next = gcds[index]
        gcds[index].next = nextNode
        index += 1
        current = nextNode
        nextNode = current.next

    return head