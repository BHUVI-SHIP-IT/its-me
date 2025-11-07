class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=0
        high=0
        for g in gain:
            alt+=g
            high=max(high,alt)
        return high
        