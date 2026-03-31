class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_array = sorted(set(nums))
        nums[:len(unique_array)-1] = unique_array
        return len(unique_array)
        