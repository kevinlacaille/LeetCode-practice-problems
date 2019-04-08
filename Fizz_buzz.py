class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        else:
            nums = []
            for i in range(1,n+1):
                if i % 3 == 0 and i % 5 == 0:
                    nums.append("FizzBuzz")
                elif i % 3 == 0:
                    nums.append("Fizz")
                elif i % 5 == 0:
                    nums.append("Buzz")
                else:
                    nums.append(str(i))
            return nums
            
