class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        behen_ji=0
        for i in words:
            if i.startswith(pref):
                behen_ji+=1
        return behen_ji
        