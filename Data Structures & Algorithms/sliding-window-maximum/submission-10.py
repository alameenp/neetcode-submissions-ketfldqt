import heapq
from collections import Counter

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        in_window = Counter()
        h = []
        output = []
        for r,c in enumerate(nums):
            heapq.heappush(h,-c)
            in_window[-c] += 1
            if r < k-1:
                continue
            while in_window[h[0]]==0:
                heapq.heappop(h)

            output.append(-h[0])
            in_window[-nums[r-k+1]]-=1
        return output


            

            


        




        
        