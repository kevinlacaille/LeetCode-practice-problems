class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """


        all_nums = range(left,right+1)
        to_del = []

        for i in all_nums:
            if len(str(i)) == 1:
            # these are automatically self-dividing
                pass
            elif i % 10 == 0:
                # these have zeros in them, not self-dividing
                to_del.append(i)

            elif len(str(i)) >1:
                for j in range(len(str(i))):
                    if int(str(i)[j]) == 0:
                        to_del.append(i)
                        break
                    if i % int(str(i)[j]) != 0:
                        to_del.append(i)

        self_divs = [x for x in all_nums if x not in to_del]

        return self_divs
