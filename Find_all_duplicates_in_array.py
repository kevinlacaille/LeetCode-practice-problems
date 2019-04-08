class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums = sorted(nums)
        residuals = []

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                residuals.append(nums[i])
        return residuals
