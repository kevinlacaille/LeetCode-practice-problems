class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # If list is empty, return a list of nothing
        if len(strs) == 0:
            anagrams = []
            return anagrams


        # Otherwise, let's begin!
        else:
            # Sort list of words
            strs_sorted = []
            for i in strs:
                strs_sorted.append(sorted(i))

            # Create indices as to where we find the words sorted
            # e.g., where do we find ['a','e','t'] in the list?
            indices = []
            if len(indices) == len(strs):
                return indices
            else:
                for j in range(len(strs_sorted)):
                    # Search for the first sorted word
                    if j == 0:
                        indices.append([i for i,x in enumerate(strs_sorted) if x==strs_sorted[0]])
                    else:
                        # If a sorted word appears in list, pass and try for the next
                        if [i for i,x in enumerate(strs_sorted) if x==strs_sorted[j]] in indices:
                            pass
                        else:
                            # Append any other words that are not already in the list
                            indices.append([i for i,x in enumerate(strs_sorted) if x==strs_sorted[j]])

        # Create list of anagrams
        anagrams = []
        for i in indices:
            tmp = []
            for j in i:
                tmp.append(strs[j])
            anagrams.append(tmp)
        return anagrams
