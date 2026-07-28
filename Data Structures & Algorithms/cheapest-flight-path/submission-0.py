from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Start with -1 for all airports (-1 means "unreachable so far")
        prices = [-1] * n
        prices[src] = 0  # Starting point costs $0

        # Step 2: At most k stops means at most k + 1 flights
        for _ in range(k + 1):
            temp_prices = list(prices)  # Make a copy for this flight log
            
            for u, v, price in flights:
                # If we haven't reached airport 'u' yet, we can't fly out of it!
                if prices[u] == -1:
                    continue
                
                new_cost = prices[u] + price
                
                # Update temp_prices if 'v' hasn't been reached yet OR if new_cost is cheaper
                if temp_prices[v] == -1 or new_cost < temp_prices[v]:
                    temp_prices[v] = new_cost
            
            prices = temp_prices  # Move to the next flight leg

        return prices[dst]