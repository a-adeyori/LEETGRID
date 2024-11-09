from collections import defaultdict
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        output=[ ]
        store1=defaultdict(set)
        store2=defaultdict(set)
        store3=defaultdict(set)

        for i,val in enumerate(nums1):
            store1[i]=val

        for i,val in enumerate(nums2):
            store2[i]=val

        for i,val in enumerate(nums3):
            store3[i]=val

        for i in store1.values():
            if i in store2.values() or i in store3.values():
                output.append(i)

        for j in store2.values():
            if j in store1.values() or j in store3.values():
                if j not in output:
                    output.append(j)

        for k in store3.values():
            if k in store1.values() or k in store2.values():
                if k not in output:
                    output.append(k)
        
        result=[q for q in set(output)]
        return result

        
#Optimized

from collections import defaultdict
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        output=[ ]
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        nums3=list(set(nums3))

        for i in nums2:
            nums1.append(i)
        for j in nums3:
            nums1.append(j)
        
        count=Counter(nums1)
        for k in count:
            if count[k]>1:
                output.append(k)

        return output
        
