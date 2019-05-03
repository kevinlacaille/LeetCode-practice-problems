class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Split a,b into real and imaginary
        a = a.split('+')
        b = b.split('+')

        # Define real and imaginary parts
        a_real = int(a[0])
        b_real = int(b[0])
        a_imaginary = int(a[1].split('i')[0])
        b_imaginary = int(b[1].split('i')[0])

        # Expanding multiplication & break into real and imaginary
        # (a+bi) + (x+yi) = a*x - b*y + (b*x + a*y)*i
        real_part  = (a_real * b_real) - (a_imaginary * b_imaginary)
        imaginary_part = (a_imaginary * b_real + a_real * b_imaginary)

        # Combine
        return str(real_part) + '+' + str(imaginary_part) + 'i'
        
