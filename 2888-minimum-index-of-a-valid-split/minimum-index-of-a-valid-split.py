class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
         counter1=collections.Counter()
         counter2=collections.Counter(nums)
         for i,num in enumerate(nums):
            counter1[num]=counter1[num]+1
            counter2[num]=counter2[num]-1
            if counter1[num]*2>i+1 and counter2[num]*2>len(nums)-i-1:
                return i
         return -1   
            
        
            
            
            
            
            
        