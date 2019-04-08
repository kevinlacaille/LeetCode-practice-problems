class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def rotate(l, n):
                return l[-n:] + l[:-n]

        if A == []:
            return 0

        else:
            nums = []

            for j in range(len(A)):
                tot=0
                for i,a in enumerate(rotate(A,j)):
                    tot += i*a
                nums.append(tot)

            return max(nums)
