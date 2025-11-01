class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        abbey=0
        for i in words:
            if s.startswith(i):
                abbey+=1
        return abbey
        