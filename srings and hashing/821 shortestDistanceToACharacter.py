class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        answer=[]
        
        target = []

        for i in range(len(s)):
            if s[i] == c:
                target.append(i)

        mini=float("Inf")

        for i in range(len(s)):
            if s[i]!=c:
                for j in range(len(target)):
                    mini = min(mini, abs(i-target[j]))
                answer.append(mini)
                mini=float("Inf")
            else:
                answer.append(0)
        
        return answer
