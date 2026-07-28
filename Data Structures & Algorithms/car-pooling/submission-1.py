import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return 0
        trips.sort(key=lambda x: x[1])
        min_heap = []
        curr_pass = 0
        for num_passengers, start_loc, end_loc in trips:
            while min_heap and min_heap[0][0] <= start_loc:
                dropped_end, dropped_pass = heapq.heappop(min_heap)
                curr_pass -= dropped_pass

            # 2. PICK UP: Add the new passengers to the car
            curr_pass += num_passengers
            heapq.heappush(min_heap, (end_loc, num_passengers))

            # 3. CAPACITY CHECK: Did we overload the car?
            if curr_pass > capacity:
                return False
        return True
         