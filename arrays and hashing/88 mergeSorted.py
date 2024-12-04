#my own solution lol 10ms
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums2Pointer=0
        m==m

        for i in range(len(nums1)):
            if i==m and nums1[i]==0:
                nums1[i]=nums2[nums2Pointer]
                nums2Pointer+=1
                m+=1

        print(nums1)
        nums1Output = sorted(nums1)
        diff = len(nums1Output)-len(nums1)

        i=1

        while i < diff:
            nums1.pop()
            i+=1

        for i in range(len(nums1)):
            nums1[i] = nums1Output[i]
