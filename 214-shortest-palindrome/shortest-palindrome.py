class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ulta_panthi=s[::-1]
        for i in range(len(s)+1):
            if s.startswith(ulta_panthi[i:]):
                return ulta_panthi[:i]+s
        

        