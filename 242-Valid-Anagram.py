from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check if lengths are different
        if len(s) != len(t):
            return False
        
        # Step 2: Count characters in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Step 3: Compare counts
        return count_s == count_t
