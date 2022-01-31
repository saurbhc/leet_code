# Link: https://leetcode.com/problems/middle-of-the-linked-list/

# Time Complexity: O(n)
# Space Complexity: O(n)
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        all_nodes = [head]

        while head.next:
            all_nodes.append(head.next)
            head = head.next

        return all_nodes[len(all_nodes) // 2]
