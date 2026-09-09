class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_pos=bisect_left(nums,target)
        second_pos=bisect_right(nums,target)
        if first_pos==second_pos:
            return [-1,-1]
        else:
            return(first_pos,second_pos-1)
       