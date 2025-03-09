class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        for i in range(n):
            for j in range(n):
                if (baskets[j]>=fruits[i]):
                    baskets[j]=0
                    break
        count=0
        for h in baskets:
            if h!=0:
                count+=1
        return count
        