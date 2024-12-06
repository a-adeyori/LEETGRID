class Solution(object):
    def thirdMax(self, nums):
        store=list(set(nums))
        store.sort()
        if len(store)>=3:
            store.pop()
            store.pop()
            return store.pop()
        else:
            return max(store)