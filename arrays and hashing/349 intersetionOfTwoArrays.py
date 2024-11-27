class Solution(object):
    def intersection(self, nums1, nums2):
        set_nums1=set(nums1)
        set_nums2=set(nums2)
     
        return list(set_nums1&set_nums2)