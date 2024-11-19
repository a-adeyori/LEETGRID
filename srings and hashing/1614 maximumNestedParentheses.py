class Solution(object):
    def maxDepth(self, s):
        stack=[]
        store=[]
        count=0

        if '(' not in s or ')' not in s:
            return 0
            
        for p in s:
            if stack and p==')' and stack[-1]=='(':
                store.append(count)
                stack.pop(-1)
                count=len(stack)
                
            elif p=='(':
                stack.append(p)
                count+=1
        return max(store)