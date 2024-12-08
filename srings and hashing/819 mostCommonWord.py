import re
from collections import defaultdict, Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        #short and learnt the fuction most_common in Counter
        newWords = re.findall(r"[a-zA-Z]+", paragraph.lower())
        
        counter = Counter(word for word in newWords if word not in banned)

        return counter.most_common(1)[0][0]

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