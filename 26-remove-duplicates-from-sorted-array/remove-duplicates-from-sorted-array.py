class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=sorted(set(nums))
        for i in range(len(res)):
            nums[i]=res[i]
        return len(res)