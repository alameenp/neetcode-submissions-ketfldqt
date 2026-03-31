class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left < right:
            l_num = numbers[left]
            r_num = numbers[right]
            s = l_num+r_num
            if target == s:
                return [left+1,right+1]
            if target < s :
                right -= 1
                continue
            if target > s:
                left+=1
                continue
