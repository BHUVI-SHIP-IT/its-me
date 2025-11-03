class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_t=0
        for i in range(1,len(colors)):
            if colors[i]==colors[i-1]:
                total_t+=min(neededTime[i],neededTime[i-1])
                neededTime[i]=max(neededTime[i],neededTime[i-1])
        return total_t

        