class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        total = []
        if len(S) > 0:
            for j in J:
                for s in S:
                    if j==s:
                        total.append(j)
                    else:
                        pass
            return len(total)
        else:
            return 0
