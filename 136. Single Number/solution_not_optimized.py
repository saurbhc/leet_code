# Link: https://leetcode.com/problems/single-number/

# Time Complexity: O(2n)
# ... Constructing Counter is O(n)
# ... then iterating on counter is O(n)
# Space Complexity: O(n)
import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        for key, value in counts.items():
            if value == 1:
                return key
