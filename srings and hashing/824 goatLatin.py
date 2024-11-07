class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        store=[]
        output=[]
        
        words = sentence.split(' ')

        for word in words:
            if word[0].lower() in 'aeiou':
                store.append(word+'ma')
            else:
                store.append(word[1:]+word[0]+'ma')
        
        for j in range(len(store)):
            output.append(store[j]+('a'*(j+1)))

        return ' '.join(output)



