# Link: https://leetcode.com/problems/palindrome-linked-list/

# Time Complexity: O(n)
# Space Complexity: O(1)
# ... as it is a Singly-list-list, idea here is:
# ... - find middle (by slow and fast pointers)
# ... - reverse second half (reverse linked list algo)
# ... - check palindrome
# Definition for singly-linked list.
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
