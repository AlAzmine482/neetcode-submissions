"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # 1. Sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals: 
            # 2. Check if the earliest-ending meeting has finished
            # (min_heap[0] is always the smallest end time in the heap)
            if min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)  # Free up that room!
                
            # 3. Add THIS meeting's end time to reserve/occupy a room
            heapq.heappush(min_heap, interval.end)

        # The count of end times remaining in the heap is the min rooms needed
        return len(min_heap)