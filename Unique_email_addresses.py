class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        newEmails = []
        for email in emails:
            # split for local name only
            # ignore everything after the "@"
            # ignore everything after the "+"
            # join everything with "."
            local = "".join(email.split('@')[0].split('+')[0].split('.'))

            # split for domain name only
            # ignore everything before the "@"
            # include the "+"
            # include the "."
            domain = email.split('@')[1]

            # combine the local + '@' + domain
            newEmails.append(local+'@'+domain)

        # create a set and measure length to see how many are not duplicates
        return len(set(newEmails))        
