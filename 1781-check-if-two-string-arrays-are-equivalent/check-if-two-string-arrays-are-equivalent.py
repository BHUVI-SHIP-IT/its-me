class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        e1=e2=""
        for i in word1:
            e1+=i
        for i in word2:
            e2+=i
        return e1==e2

        