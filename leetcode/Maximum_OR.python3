class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i] | nums[i]
        suffix=[0]*(n+1)
        for i in range(n-1,-1,-1):
            suffix[i]=suffix[i+1] | nums[i]
        max_or=0
        for i in range(n):
            shift=nums[i]<<k
            total=prefix[i] | shift | suffix[i+1]
            max_or=max(total,max_or)
        return max_or