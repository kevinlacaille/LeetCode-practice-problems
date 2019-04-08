class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        max_index = A.index(max(A))
        if max_index == len(A)-1 or max_index == 0:
                return False
        else:
            counter=0
            for i in range(len(A)):
                if i == 0:
                    if i < max_index and A[max_index]-A[i] > 0:
                        counter+=1
                else:
                    if i < max_index and A[i]-A[i-1] > 0:
                        counter+=1
                    if i == max_index and A[max_index]-A[i] == 0:
                        counter+=1
                    elif i > max_index and A[i-1]-A[i] > 0:
                        counter+=1
            print len(A),counter

            if len(A) == counter:
                return True
            else:
                return False
