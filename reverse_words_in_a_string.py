class Solution(object):
    def reverseWords(self, text):
        text = str(text)
        return ' '.join(text.split()[::-1])
