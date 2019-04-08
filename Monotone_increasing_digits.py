class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 10:
            return N

        else:
            isTrue = False
            while isTrue != True:
                num = map(int, str(N))
                if num == sorted(num):
                    isTrue = True
                else:
                    N -= 1
            return N    
