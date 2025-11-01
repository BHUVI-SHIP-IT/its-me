class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        lol=target[0]
        for i in range(1,len(target)):
            lol+=max(target[i]-target[i-1],0)
        return lol
        
        