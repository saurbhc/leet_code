# Link: https://leetcode.com/problems/linked-list-cycle/

# Time Complexity: O(n)
# Space Complexity: O(1)
# ... here, we are modifying the LinkedList

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        while head:
            if head.val is False:
                return True

            head.val = False
            head = head.next

        return False
