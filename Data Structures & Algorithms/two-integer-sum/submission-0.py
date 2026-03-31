class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,val in enumerate(nums):
            compliment = target - val
            if compliment in seen:
                return [seen[compliment],index]
            seen[val] = index
        
            
                    


    
                



        