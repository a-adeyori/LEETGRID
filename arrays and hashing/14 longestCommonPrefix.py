class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs==[]:
            return ''
        
        prefix=strs[0]

        for i in range(len(strs)):
            while not strs[i].startswith(prefix):
                prefix=prefix[:-1]
        return prefix

    

    

        