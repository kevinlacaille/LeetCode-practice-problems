class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]

        else:
            where = []
            # Search from the left side
            for i in range(len(nums)):
                if nums[i] == target:
                    where.append(i)
                    break
            # Search from right side
            for i in range(len(nums))[::-1]:
                if nums[i] == target:
                    where.append(i)
                    break
            return where
