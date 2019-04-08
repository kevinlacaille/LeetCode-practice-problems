class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        prime_pals = []
        '''
        Here's an idea:
        Iteratively check through a list of primes, not just any numbers between
        2 and sqrt(possiblePrime), since it will only be a factor of two primes
        '''
        #star checking here
        possiblePrime = 2
        while possiblePrime <= int(1e8):
            # Assume number is prime until shown it is not.
            isPrime = True
            # search between 2 and the square root of the number,
            # since no factor can be larger than the number it self
            for num in range(2, int(possiblePrime**0.5+1)):
                if possiblePrime % num == 0:
                    # found a non-prime, break the loop
                    isPrime = False
                    break
            # found a prime
            if isPrime:
                # is the prime a palindrome?
                if str(possiblePrime)[::-1] == str(possiblePrime):
                    # yes it is, append it!
                    prime_pals.append(possiblePrime)

            # if the last prime palindrom >= N break loop
            if len(prime_pals)>0 and prime_pals[-1] >= N:
                break
            else:
                possiblePrime+=1

        # return largest prime pal >= N
        return prime_pals[-1]
