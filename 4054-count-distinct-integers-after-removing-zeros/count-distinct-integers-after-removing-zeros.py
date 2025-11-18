class Solution:
    def countDistinct(self, n: int) -> int:
        s=str(n)
        l=len(s)
        res=0
        pow9=1
        for k in range(1,l):
            pow9*=9
            res+=pow9
        for i,ch in enumerate(s):
            d=int(ch)
            rem=l-1-i
            choices=max(0,d-1)
            res+=choices*(9**rem)
            if d==0:
                return res
        return res+1
        