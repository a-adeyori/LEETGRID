from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        store=defaultdict(int)
        pos=[]

        for i in range(len(s)):
            store[s[i]]+=1

        for key,value in store.items():
            if value==1:
                pos.append(s.index(key))
            
        least=min(pos) if pos else -1
            
        return least