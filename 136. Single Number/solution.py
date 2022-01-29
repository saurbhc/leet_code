# Link: https://leetcode.com/problems/single-number/

# Time Complexity: O(n)
# ... iterating on nums is O(n)
# Space Complexity: O(1)
import functools
import operator
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # result = 0
        # for n in nums:
        #     result ^= n

        # return result

        return functools.reduce(operator.xor, nums)
