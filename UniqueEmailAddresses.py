# https://leetcode.com/problems/unique-email-addresses
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()
        for email in emails:
            name, domain = email.split('@') 
            local = name.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)