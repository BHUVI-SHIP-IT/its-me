class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow={}
        cons={}
        for c in s:
            if c in "aeiouAEIOU":
                vow[c]=vow.get(c,0)+1
            else:
                cons[c]=cons.get(c,0)+1
        max_v=max(vow.values()) if vow else 0
        max_c=max(cons.values()) if cons else 0
        return max_c+max_v

        