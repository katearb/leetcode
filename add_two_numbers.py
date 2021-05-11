# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def _create(res, i=1):
        if len(res) == i:
            return ListNode(int(res[0]))
        return ListNode(int(res[-i]), Solution._create(res, i + 1))

    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = power1 = power2 = 0

        while l1:
            n1 += l1.val * (10 ** power1)
            power1 += 1
            l1 = l1.next

        while l2:
            n2 += l2.val * (10 ** power2)
            power2 += 1
            l2 = l2.next

        return Solution._create(str(n1+n2))
