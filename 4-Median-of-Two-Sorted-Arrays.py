class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array=sorted(nums1+nums2)
        n=len(merged_array)
        if n%2==1:
            return merged_array[n//2]
        else:
            return (merged_array[n//2-1] + merged_array[n//2])/2