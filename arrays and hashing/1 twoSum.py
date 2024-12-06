import collections
class Solution(object):
    #look up method
    def twoSum(self, nums, target):
        prevMap=collections.defaultdict(int)
        for i,n in enumerate(nums):
            diff= target-n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n]=i