class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        max1=max2=float('-inf')
        mini=float('inf')
        for x in nums:
            if x>max1:
                max2=max1
                max1=x
            elif x>max2:
                max2=x
            if x<mini:
                mini=x
        return max1+max2-mini
        