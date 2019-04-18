class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_reverse = []
        for i in s.split():
            s_reverse.append(i[::-1])

        return ' '.join(s_reverse)
