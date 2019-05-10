class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Finds the tallest mountain in the mountain range
        return A.index(max(A))

        # ''''''Option 2: Simply finds the first "mountain" in mountain range''''''
        # for i in xrange(len(A)):
        #     if A[i] > A[i+1]:
        #         return i
