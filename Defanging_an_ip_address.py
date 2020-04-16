class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        split_address = address.split(".")
        bracket_dot = "[.]"
        defanged_IP = ""
        
        for i in range(len(split_address)):
            if i != len(split_address) - 1:
                defanged_IP += str(split_address[i]) + bracket_dot
            else:
                defanged_IP += str(split_address[i])        
                
        return defanged_IP
