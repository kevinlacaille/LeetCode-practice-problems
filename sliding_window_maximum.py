class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k > len(nums):
            return max(nums)
        else:
            window_max = []
            for i in xrange(len(nums)):
                if i > len(nums) - k:
                    break
                else:
                    window_max.append(max(nums[i:i+k]))
            return window_max
            
