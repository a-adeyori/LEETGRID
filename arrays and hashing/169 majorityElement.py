import collections
class Solution(object):
    def majorityElement(self, nums):
        store= collections.defaultdict(int)
        for i in nums:
            store[i]+=1

        for i,n in store.items():
            if n>len(nums)/2:
                return i