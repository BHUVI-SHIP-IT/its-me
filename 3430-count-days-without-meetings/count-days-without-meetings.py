class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        free_days=0
        prev_days=0
        for start,end in sorted(meetings):
            if start>prev_days:
                free_days+=start-prev_days-1
            prev_days=max(prev_days,end)
        return free_days+max(0,days-prev_days)
        
        