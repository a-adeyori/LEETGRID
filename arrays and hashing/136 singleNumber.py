from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        store=defaultdict(int)
        
        for i in range(len(nums)):
            store[nums[i]]+=1
        
        for key,value in store.items():
            if value==1:
                return key