class Solution:
    def isNumber(self, s: str) -> bool:
        n=len(s)
        i=0
        seen_digit=False
        seen_dot=False
        seen_exp=False
        while i<n:
            c=s[i]
            if c.isdigit():
                seen_digit=True
            elif c in '+-':
                if i>0 and s[i-1] not in 'eE':
                    return False
            elif c=='.':
                if seen_dot or seen_exp:
                    return False
                seen_dot=True
            elif c in 'eE':
                if seen_exp or not seen_digit:
                    return False
                seen_exp=True
                seen_digit=False
            else:
                return False
            i+=1
        return seen_digit
