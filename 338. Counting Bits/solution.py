# Link: https://leetcode.com/problems/counting-bits/

# Time Complexity: O(n*k)
# Space Complexity: O(n)
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]

        while len(output) <= n:
            output.extend([i+1 for i in output])

        return output[:n+1]
