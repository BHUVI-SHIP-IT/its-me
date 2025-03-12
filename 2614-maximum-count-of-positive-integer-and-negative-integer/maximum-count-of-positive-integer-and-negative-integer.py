class Solution(object):
    def maximumCount(self, nums):
        post=0
        negt=0
        for n in nums:
            if(n<0):
                negt+=1
            elif(n>0):
                post+=1
        return max(post,negt)
        """
        :type nums: List[int]
        :rtype: int
        """
        