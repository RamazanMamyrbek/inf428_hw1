class Solution(object):
    def findLengthOfLCIS(self, nums):
        numCount = 1
        maxLength = 1
        for i in range(0, len(nums)-1):
            if nums[i] < nums[i+1]:
                numCount += 1
            else:
                numCount = 1
            maxLength = max(maxLength, numCount)
        return maxLength