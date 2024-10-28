from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        store=defaultdict(list)
        for word in strs:
            count=[0]*26
            for c in word:       
                 count[ord(c)-ord('a')]+=1
            store[tuple(count)].append(word)
        return store.values()


        
        