class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        isTrue = False
        for i in matrix:
            if target in i:
                isTrue = True

        return isTrue
