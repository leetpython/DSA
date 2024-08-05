from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            # The reference to curr.next will be lost on
            # reversing the prev → curr link, so store it temporarily
            next = curr.next

            # Reverse the prev → curr link
            curr.next = prev

            prev = curr
            curr = next

        return prev
