# Link: https://leetcode.com/problems/contains-duplicate/

# (if n denotes to counts of numbers in nums)
# Time Complexity: O(n)
# ... In each iteration, search and insertion of the hash set both takes
# ... O(logn) time in worst case and O(1) time in average cases
# ... Therefore, it’s takes O(n * (2logn)) = O(nlogn) time in worst case
# ... but O(n) time in average cases.
# Space Complexity: O(n)
# ... it uses O(n) extra space for maintaining this hash set
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for n in nums:
            if n in hash_set:
                return True

            hash_set.add(n)

        return False
