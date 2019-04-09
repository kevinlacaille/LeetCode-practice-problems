class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A_squared = []
        for a in A:
            A_squared.append(a**2)
        A_squared.sort()
        return A_squared
