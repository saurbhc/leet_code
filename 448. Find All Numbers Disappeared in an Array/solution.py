# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Time Complexity: O(3n)
# ... best case: O(2n)
# Space Complexity: O(2n)
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1, len(nums) + 1)).difference(set(nums))
