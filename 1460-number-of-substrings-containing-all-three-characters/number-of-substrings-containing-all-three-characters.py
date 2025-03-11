class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count={'a':0,'b':0,'c':0}
        left=0
        right=0
        result=0
        while right<len(s):
            count[s[right]]+=1
            while count['a']>0 and count['b']>0 and count['c']>0:
                count[s[left]]-=1
                result+=len(s)-right
                left+=1
            right+=1
        return result
        