import heapq
from collections import Counter

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        in_window = Counter()
        h = []
        output = []
        for r,c in enumerate(nums):
            if r - l + 1 < k:
                in_window[-c] += 1
                heapq.heappush(h,-c)
                r+=1
                continue
            heapq.heappush(h,-c)
            in_window[-c] += 1
            j=0
            while j <= r:
                max_value = h[0]
                if in_window[max_value] > 0:
                    output.append(-max_value)
                    break
                heapq.heappop(h)
            in_window[-nums[l]]-=1
            l+=1
        return output


            

            


        




        
        