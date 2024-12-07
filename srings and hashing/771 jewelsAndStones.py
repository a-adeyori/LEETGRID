from collections import defaultdict
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        #short and syntax based
        return sum(stones.count(i) for i in jewels)
    
        #logic and understandable
        store=defaultdict(int)

        for i in stones:
            if i in jewels:
                store[i]+=1
        sum=0
        for values in store.values():
            sum+=values
        return sum