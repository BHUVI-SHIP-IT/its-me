from collections import Counter

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        result = []
        
        
        for i in range(len(nums) - k + 1):
            
            subarray = nums[i:i + k]
            
            
            freq = Counter(subarray)
            
           
            sorted_elements = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            
            
            x_sum = 0
            count = 0
            
            for num, count_num in sorted_elements:
                if count < x:
                    x_sum += num * count_num
                    count += 1
            
            
            result.append(x_sum)
        
        return result

        