class Solution:
    def reverse(self, x: int) -> int:
        
        # If negative, remove negative sign
        if str(x).find('-') == 0:
            reversed_x = int('-' + str(x)[::-1][:-1])
        else:
            reversed_x = int(str(x)[::-1])
            
        # reversed_x must be a <32-bit integer
        if reversed_x.bit_length() >= 32:
            return 0
        else:
            return reversed_x
