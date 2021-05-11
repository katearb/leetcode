# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
        first_head = second_head = head

        for _ in range(n):
            first_head = first_head.next

        if not first_head:
            return head.next

        while first_head.next:
            second_head = second_head.next
            first_head = first_head.next

        second_head.next = second_head.next.next

        return head
