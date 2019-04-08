class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        if zeros > 0:
            for i in range(0,zeros):
                nums.remove(0)
                nums.append(0)
