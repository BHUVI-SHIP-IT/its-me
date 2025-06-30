class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq = {}
        
        # Count the frequency of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        longest = 0
        # Iterate through the keys in the frequency dictionary
        for key in freq:
            if key + 1 in freq:  # Check if the consecutive number exists
                longest = max(longest, freq[key] + freq[key + 1])
        
        return longest

        