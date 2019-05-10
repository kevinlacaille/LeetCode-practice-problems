class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Simply finds the first "mountain" in mountain range
        for i in xrange(len(A)):
            if A[i] > A[i+1]:
                return i
