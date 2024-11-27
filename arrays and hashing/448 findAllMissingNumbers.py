class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        all_nums = set(range(1,n+1))
        print(all_nums)
        new_nums = set(nums)
        print(new_nums)
        diff = list(all_nums- new_nums)
        print(diff)

        return diff