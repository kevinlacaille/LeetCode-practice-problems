class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # col_1[::-1] -> row_1
        # col_2[::-1] -> row_2
        # ...
        # col_n[::-1] -> row_n


        '''
        # Here's a method to create a new image
        rot_matrix = []
        for i in range(len(matrix)):
            new_row = []
            for j in range(len(matrix[i])):
                new_row.append(matrix[j][i])
            rot_matrix.append(new_row[::-1])

        return rot_matrix
        '''
        # Flip the matrix upsidown, about the centre (e.g., row_1 = row_n, row_2 = row_n-1, etc.)
        # This is the same as mastrix[::-1]
        matrix.reverse()

        # Seach through each row
        # Note that using xrange vs. range, so to not generate a list, to save memory
        for i in xrange(len(matrix)):
            # For each row
            for j in xrange(i + 1, len(matrix)):
                # Swap matrix positions
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
