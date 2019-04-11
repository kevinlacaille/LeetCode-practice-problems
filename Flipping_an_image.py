class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # reverse each row
        for i in A:
            i.reverse()

        # convert 1's to 0's and 0's to 1's
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1

        return A
