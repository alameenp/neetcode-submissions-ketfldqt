class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left < right:
            l_num = numbers[left]
            r_num = numbers[right]
            if target - r_num == l_num:
                return [left+1,right+1]
            if target - r_num < l_num:
                right -= 1
                continue
            if target - r_num > l_num:
                left+=1
                continue
