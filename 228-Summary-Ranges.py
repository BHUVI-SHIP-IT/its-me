from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            # Check if nums[i] is not consecutive with nums[i-1]
            if nums[i] != nums[i - 1] + 1:
                # Add the current range to the list
                if start == nums[i - 1]:
                    ranges.append(f\{start}\)
                else:
                    ranges.append(f\{start}->{nums[i - 1]}\)
                # Update start to the current number
                start = nums[i]

        # Add the last range
        if start == nums[-1]:
            ranges.append(f\{start}\)
        else:
            ranges.append(f\{start}->{nums[-1]}\)
        
        return ranges


        