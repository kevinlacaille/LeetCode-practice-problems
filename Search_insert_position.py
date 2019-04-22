nums = [1,3,5,6]
target = 0

if target in nums:
    for i,a in enumerate(nums):
        if a == target:
            print i
            break
if target not in nums:
    if nums[-1] < target:
        print len(nums)
    else:
        for i,a in enumerate(nums):
            if a - target < 0:
                pass
            else:
                print i
                break
