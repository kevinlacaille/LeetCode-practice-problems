class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if nums == [] or nums == [0]:
            return 1
        ## Doesn't work for single value arrays
        ## E.g., [2147483647]
        
        import numpy as np

        # Sort data, remove duplicates, and make nums an array
        nums = np.sort(np.array(list(set(nums))))
        # Only select positive numbers
        nums = nums[np.where(nums > 0)[0]]
        
        
        all_possible_nums = np.arange(1, nums[-1] + 1)
        
        first_missing_positive = set(all_possible_nums) - set(nums)        
        first_missing_positive = [int(i) for i in first_missing_positive]
        
        if not np.array(first_missing_positive).any():
            return nums[-1] + 1
        else:
            first_missing_positive = first_missing_positive[0]
            return first_missing_positive
            
