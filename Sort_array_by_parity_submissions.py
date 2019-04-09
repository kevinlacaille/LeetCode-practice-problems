class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A_even = []
        A_odd = []
        for a in A:
            if a % 2 == 0:
                A_even.append(a)
            else:
                A_odd.append(a)
        return A_even + A_odd
