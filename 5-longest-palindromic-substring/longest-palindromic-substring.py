class Solution:
    def longestPalindrome(self, s: str) -> str:
        def see(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        long_sub=""
        for i in range(len(s)):
            temp=see(i,i)
            if(len(temp)>len(long_sub)):
                long_sub=temp
            temp=see(i,i+1)
            if(len(temp)>len(long_sub)):
                long_sub=temp
        return long_sub

        