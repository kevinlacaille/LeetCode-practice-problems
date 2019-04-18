class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']

        s_new = []
        index = 1
        for i in S.split():
            if i[0] in vowel:
                s_new.append(i+'ma'+index*'a')
            else:
                s_new.append(i[1:]+i[0]+'ma'+index*'a')
            index+=1

        return ' '.join(s_new)
