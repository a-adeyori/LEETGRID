import collections
def isAnagram(s, t):
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
                