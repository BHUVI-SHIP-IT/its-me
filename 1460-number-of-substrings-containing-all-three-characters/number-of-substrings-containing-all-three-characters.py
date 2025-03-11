class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count_a=0
        count_b=0
        count_c=0
        count=0
        right=0
        left=0
        n=len(s)
        while right<n:
            if s[right]=='a':
                count_a+=1
            elif s[right]=='b':
                count_b+=1
            elif s[right]=='c':
                count_c+=1
            while count_a>0 and count_b>0 and count_c>0:
                if s[left]=='a':
                    count_a-=1
                elif s[left]=='b':
                    count_b-=1
                elif s[left]=='c':
                    count_c-=1
                count+=n-right
                left+=1
            right+=1
        return count

        