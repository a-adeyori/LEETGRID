import re
from collections import defaultdict
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        #my brute force :/
        store=defaultdict(int)
        newWords = re.findall(r"[a-zA-Z]+", paragraph.lower())
        
        for j in newWords:
            if j not in banned:
                store[j.lower()]+=1 

        maximum = max(store.values()) 

        for key,val in store.items():
            if val == maximum:
                return key