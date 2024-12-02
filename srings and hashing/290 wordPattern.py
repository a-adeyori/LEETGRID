from collections import defaultdict
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        list_s=[]
        
        store=defaultdict(str)
        list_pattern=[]

        if len(pattern)!=len(s.split(' ')):
            return False

        for i in pattern:
            if i not in list_pattern:
                list_pattern.append(i)
            else:
                continue
        
        for i in s.split(' '):
            if i not in list_s:
                list_s.append(i)
            else:
                continue


        for i,j in zip(list_pattern,list_s):
            store[j]=i

        print(store)

        for i,j in zip(pattern,s.split(' ')):
            if store[j]!=i:
                return False
        return True