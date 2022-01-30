# Link: https://leetcode.com/problems/climbing-stairs/

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            one, two = one + two, one

        return one
