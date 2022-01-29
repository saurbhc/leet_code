# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Time Complexity: O(n)
# Space Complexity: O(1)
# ... [You may assume the returned list does not count as extra space.]
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            position = abs(n) - 1
            # mark n-1 index of nums as negative number
            if nums[position] < 0:
                # already marked
                continue
            else:
                # mark the number (update the n-1 by multplying it by -1)
                nums[position] *= -1

        # find the elements which are positive, from nums array
        result = []
        for i, n in enumerate(nums):
            if n > 0:
                result.append(i+1)

        return result
