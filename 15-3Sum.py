class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        result = []
        n = len(nums)
        
        for i in range(n):
            # Step 2: Skip duplicate elements for the fixed number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # Step 3: Found a triplet, add it to the result
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Step 4: Skip duplicates for the second and third numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
                
                elif total < 0:
                    # If the sum is less than zero, move the left pointer to the right
                    left += 1
                else:
                    # If the sum is greater than zero, move the right pointer to the left
                    right -= 1
        
        return result

        