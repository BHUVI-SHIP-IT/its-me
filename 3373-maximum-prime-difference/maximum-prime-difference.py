class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isprime(num):
            if num<2:
                return False
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    return False
            return True
        prime_indices=[]
        for i,num in enumerate(nums):
            if isprime(num):
                prime_indices.append(i)
        highest=prime_indices[0]
        lowest=prime_indices[-1]
        return abs(highest-lowest)
        