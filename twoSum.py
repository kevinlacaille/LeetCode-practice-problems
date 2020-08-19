def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # Empty set for all values seen
    all_values = {}

    # Loop through all numbers in num
    for index, num in enumerate(nums):

        # Look for target - num
        value = target - num

        # If value exists in all_value,
        # return it's index and the current index
        if value in all_values:
            return [all_values[value], index]
        # Otherwise, store that index
        else:
            all_values[num] = index
            
    # If nothing adds up to target, then return  empty list
    return []

if __name__ == '__main__':
    twoSum(self, nums, target)