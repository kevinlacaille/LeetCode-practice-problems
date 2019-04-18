class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        '''
        either:
        - all cap
        - all lower
        - only 1st is cap
        '''
        # If a one letter word, capital is used correctly
        if len(word) == 1:
            return True
        # Otherwise, let's find out!
        else:
            isTrue = True
            # If a word starts off without a capital, the rest must be uncapitalized
            if word[0].isupper() == False:
                for i in range(len(word))[1:]:
                    if word[i].isupper() == True:
                        isTrue = False
                        break
                    else:
                        isTrue = True
                return isTrue

            # If a word starts ff with a capital, must be all capital, or just the first letter
            if word[0].isupper() == True:
                restCap = 0
                for i in word[1:]:
                    if i.isupper() == True:
                        restCap += 1
                if restCap == 0:
                    # Rest of the word is lowercase
                    return True
                elif len(word[1:]) == restCap:
                    # Entire word is uppercase
                    return True
                else:
                    # Some jumblled up word
                    return False
