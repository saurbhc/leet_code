# Link: https://leetcode.com/problems/range-sum-query-immutable/

# Time Complexity: O(n)
# ... O(n) for initializing the class
# ... O(n) for calculating the sum
# Space Complexity: O(1)
from typing import List
import itertools


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = list(itertools.accumulate([0] + nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]
