class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        output =''
        for i in address:
            if i == '.':
                output+='[.]'
            else:
                output+=i
        return output