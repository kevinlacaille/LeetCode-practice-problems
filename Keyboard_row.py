class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        # Define american keyboard layout
        top = ['q','w','e','r','t','y','u','i','o','p']
        middle = ['a','s','d','f','g','h','j','k','l']
        bottom = ['z','x','c','v','b','n','m']

        # List to store words that satisfy requirements
        alphabet_words = []

        # Create a list of sets of each word split my letter
        word_sets = [set(s) for s in words]

        # Search through each set of word to see if they match to a set of keys
        for i in range(len(word_sets)):
            isTrueTop = 0
            isTrueMiddle = 0
            isTrueBottom = 0
            for j in word_sets[i]:
                if j.lower() in top:
                    isTrueTop += 1
                elif j.lower() in middle:
                    isTrueMiddle += 1
                elif j.lower() in bottom:
                    isTrueBottom += 1

            if isTrueTop == len(word_sets[i]) or isTrueMiddle == len(word_sets[i]) or isTrueBottom == len(word_sets[i]):
                alphabet_words.append(words[i])

        return alphabet_words
