class Solution:
    def compressedString(self, word: str) -> str:
        n=len(word)#finding the length of the given string
        ans=[]#creating an empty stack later for appending
        i=0
        j=0
        while i<n:#while l is less than n
            count=0#intialising the count to zero
            while j<n and word[j]==word[i] and count<9:
                j+=1
                count+=1
            ans.append(str(count)+word[i])#appending first string with str count on ans
            i=j
        return''.join(ans)

            
        
        