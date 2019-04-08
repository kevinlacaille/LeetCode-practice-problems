class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set(nums) only shows one of each.
        # doubling the sets will double each number.
        # assuming all numbers are doubled, except for one means
        # that we can sum up the doubled set and the sum of the
        # list and find the residual
        # the residual will be what isn't doubled!

        return 2*sum(set(nums)) - sum(nums)
