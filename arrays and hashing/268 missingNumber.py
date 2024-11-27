class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            if i in nums:
                continue
            else :
                return i

#better runtime
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        all_nums = set(range(1,n+1))
        print(all_nums)
        new_nums = set(nums)
        print(new_nums)
        diff = list(all_nums- new_nums)
        print(diff)

        if diff == []:
            return 0
            
        for x in diff:
            return x