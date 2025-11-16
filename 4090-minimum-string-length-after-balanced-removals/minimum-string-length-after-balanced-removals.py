class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        return abs(s.count('a')-s.count('b'))
        