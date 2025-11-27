class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        nums.sort()
        def back(index):
            res.append(subset[:])
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                subset.append(nums[i])
                back(i+1)
                subset.pop()
        back(0)
        return res
                

        