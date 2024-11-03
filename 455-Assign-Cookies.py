from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort greed factors of children
        s.sort()  # Sort sizes of cookies
        child_i = 0  # Pointer for children
        cookie_j = 0  # Pointer for cookies
        # Try to assign each cookie to the appropriate child
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:  # If the cookie satisfies the child
                child_i += 1  # Move to the next child
            cookie_j += 1  # Move to the next cookie
        return child_i  # The number of satisfied children

        