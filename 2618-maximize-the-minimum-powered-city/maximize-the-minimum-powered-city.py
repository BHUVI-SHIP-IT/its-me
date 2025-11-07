class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n=len(stations)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+stations[i]
        power=[0]*n
        for i in range(n):
            left=max(0,i-r)
            right=min(n-1,i+r)
            power[i]=prefix[right+1]-prefix[left]
        def can_achieve(min_power):
            extra=[0]*(n+1)
            used=0
            window_sum=0
            for i in range(n):
                if i>0:
                    window_sum+=extra[i]
                if power[i]+window_sum<min_power:
                    need=min_power-(power[i]+window_sum)
                    if used+need>k:
                        return False
                    used+=need
                    window_sum+=need
                    end=i+2*r+1
                    if end<n:
                        extra[end]-=need
            return True
        low,high=min(power),sum(stations)+k
        result=low
        while low<=high:
            mid=(low+high)//2
            if can_achieve(mid):
                result=mid
                low=mid+1
            else:
                high=mid-1
        return result
        
