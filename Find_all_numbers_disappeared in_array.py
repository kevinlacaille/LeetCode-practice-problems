class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if nums == []:
            return []
        else:
            nums = sorted(nums)
            complete_list = range(1,len(nums)+1)
            incomplete_list = list(set(nums))
            return list(set(complete_list) - set(incomplete_list))
