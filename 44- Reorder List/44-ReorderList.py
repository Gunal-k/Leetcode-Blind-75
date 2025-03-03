from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = None
        slow.next = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        second = prev
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

# Helper function to print the list (for testing purposes)
def print_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Create a linked list 1 -> 2 -> 3 -> 4
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    print("Original list:")
    print_list(head)

    # Reorder the list
    Solution().reorderList(head)

    print("Reordered list:")
    print_list(head)