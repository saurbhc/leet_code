# Link: https://leetcode.com/problems/palindrome-linked-list/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        my_list = []
        while head:
            my_list.append(head.val)
            head = head.next

        left, right = 0, len(my_list) - 1
        while left <= right:
            if my_list[left] != my_list[right]:
                return False

            left += 1
            right -= 1

        return True
