class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        mini=min(nums)
        maxe=max(nums)
        ans=[]
        for i in range(mini,maxe+1):
            if i not in nums:
                ans.append(i)
        return ans