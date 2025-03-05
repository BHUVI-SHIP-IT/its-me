class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:
            return 1
        else:
            return n**2+(n-1)**2

            