class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        import numpy as np

        customer_wealth = [] #np.zeros([1, len(accounts)])

        for i in range(len(accounts)):
            customer = accounts[i]
            customer_wealth.append(np.sum(customer))
        
        return np.max(customer_wealth)
