class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #Sliding Window
        maxAverage = -1000000
        left = 0
        currentsum = 0
        for right in range(len(nums)):
            currentsum += nums[right]
            if right >= k-1:
                avg = float(currentsum)/k
                maxAverage = max(avg,maxAverage)
                currentsum -= nums[left]
                left += 1
        return maxAverage