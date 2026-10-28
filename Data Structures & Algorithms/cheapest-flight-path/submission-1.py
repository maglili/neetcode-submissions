class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        price = [float("inf")] * n
        price[src] = 0

        for _ in range(k + 1):
            last_price = price.copy()

            for s, d, p in flights:
                if price[s] == float("inf"):
                    continue
                last_price[d] = min(last_price[d], price[s] + p)

            price = last_price

        return price[dst] if price[dst] != float("inf") else -1
