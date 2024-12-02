class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        listS=list(s)
        left=0
        right=len(s)-1

        while left<right:
            if listS[left] not in 'aeiouAEIOU':
                left+=1
            elif listS[right] not in 'aeiouAEIOU':
                right-=1
            elif listS[left] in 'aeiouAEIOU' and listS[right] in 'aeiouAEIOU':
                listS[left],listS[right]=listS[right],listS[left]
                left+=1
                right-=1
        return ''.join(listS)

#optimized solution
def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = set('aeiouAEIOU')
    listS = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and listS[left] not in vowels:
            left += 1
        while left < right and listS[right] not in vowels:
            right -= 1
        
        if left < right:
            listS[left], listS[right] = listS[right], listS[left]
            left += 1
            right -= 1
    
    return ''.join(listS)