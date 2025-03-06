class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = [1]+[0]*len(grid)**2
        for row in grid:
            for num in row:
                count[num]+=1
        return [count.index(2),count.index(0)]