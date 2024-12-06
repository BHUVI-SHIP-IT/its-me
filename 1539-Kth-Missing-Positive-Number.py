class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left=0
        right=len(arr)-1
        while(left<=right):
            mid=left+(right-left)//2
            miss=arr[mid]-(mid+1)
            if miss<k:
                left=left+1
            else:
                right=right-1
        return left+k