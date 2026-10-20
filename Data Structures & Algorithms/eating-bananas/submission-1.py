class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_max = max(piles)
        speed = k_max
        left = 1
        right = k_max
        while left<=right:
            k = (left + right)//2
            total_time = 0
            for bananas in piles:
                total_time += math.ceil(bananas/k)
            
            if total_time <= h:
                speed = k
                right = k-1
            else:
                left = k+1
        return speed

        

        

        