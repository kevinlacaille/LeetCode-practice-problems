class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # Easy solution
        # return str.lower()

        # More explicit solution
        lower_str = []
        for letter in str:
            if letter.isupper() == True:
                lower_str.append(letter.lower())
            else:
                lower_str.append(letter)
        return ''.join(lower_str)
