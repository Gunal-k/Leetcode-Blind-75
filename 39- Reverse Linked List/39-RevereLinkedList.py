# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

sol = Solution()
head1 = create_linked_list([1,2,3,4,5])
head2 = create_linked_list([1,2])
print(print_linked_list(sol.reverseList(head1))) # [5,4,3,2,1]
print(print_linked_list(sol.reverseList(head2))) # [2,1]