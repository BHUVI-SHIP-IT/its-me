class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        curr_prod=nums[0]
        min_prod=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                curr_prod,min_prod=min_prod,curr_prod
            curr_prod=max(nums[i],curr_prod*nums[i])
            min_prod = min(nums[i], min_prod * nums[i])
            max_prod=max(max_prod,curr_prod)
        return max_prod
        