
class Solution:
  def maxValue(self, events: List[List[int]], k: int) -> int:
    events.sort()
    
    num_events = len(events)
    start_days = [event[0] for event in events]

    @lru_cache(None)
    def solve(current_index: int, remaining_k: int) -> int:
      if current_index >= num_events or remaining_k == 0:
        return 0

      max_value_from_skipping = solve(current_index + 1, remaining_k)

      current_event_value = events[current_index][2]
      current_event_end_day = events[current_index][1]

      next_available_index = bisect_right(start_days, current_event_end_day)

      max_value_from_attending = current_event_value + solve(next_available_index, remaining_k - 1)
      
      return max(max_value_from_skipping, max_value_from_attending)

    return solve(0, k)