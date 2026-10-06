class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total_water = 0
        l_height = 0
        r_height = 0
        max_heights = [0]*len(height)
        ##left_height
        for i,h in enumerate(height):
            l_height = max(h,l_height)
            max_heights[i] = max(h,l_height)
        

        ## right_height
        for i in range(len(height)-1,-1,-1):
            r_height = max(height[i],r_height)
            max_heights[i] = min(r_height,max_heights[i])
        
        total_water = 0
        for i,h in enumerate(height):
            curr_water = max_heights[i]-h
            total_water+= curr_water
        return total_water


        
            
            

        
        