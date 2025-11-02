class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[str(i) for i in range(1,n+1)]
        k-=1
        result=[]
        for i in range(n,0,-1):
            fact=math.factorial(i-1)
            index=k//fact
            result.append(nums.pop(index))
            k%=fact
        return ''.join(result)
        