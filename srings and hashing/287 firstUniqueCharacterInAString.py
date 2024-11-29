from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        store=defaultdict(list)

        for i,n in enumerate(s):
            store[n].append(i)
  
        least = float('inf')
        for char, idxs in store.items():
            if len(idxs)==1:
                least=min(idxs[0],least)
        return least if least!=float('inf') else -1




        # store=defaultdict(int)
        # pos=[]

        # for i in range(len(s)):
        #     store[s[i]]+=1

        # for key,value in store.items():
        #     if value==1:
        #         pos.append(s.index(key))
            
        # least=min(pos) if pos else -1
            
        # return least