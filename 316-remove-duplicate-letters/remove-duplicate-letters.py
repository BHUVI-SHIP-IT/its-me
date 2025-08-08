class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur={}
        for i in range(len(s)):
            last_occur[s[i]]=i
        seen=set()
        result=""
        for i in range(len(s)):
            ch=s[i]
            if ch not in seen:
                while result and ch <result[-1] and i<last_occur[result[-1]]:
                    seen.remove(result[-1])
                    result=result[:-1]
                result+=ch
                seen.add(ch)
            
        return result



        