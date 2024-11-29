import collections
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        #using counter
        count_s=Counter(s)
        count_t=Counter(t)
        return count_s==count_t


        #using defaaultdict
        storeS=collections.defaultdict(int)
        storeT=collections.defaultdict(int)

        if len(s)==len(t): 
            for n in s:
                storeS[n]+=1
                
            for n in t:
                storeT[n]+=1

            for n in storeS:
                if storeS[n]!=storeT[n]:
                    return False
            return True
        
        return False