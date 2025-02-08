class Solution {
public:
    int maxVowels(string s, int k) {
        string vowels="aeiou";
        int count=0;
        int curr=0;
        int n=s.length();
        for(int i=0;i<k;i++)
        {
            if(vowels.find(s[i])!=string ::npos)
            {
                curr++;
            }
        }
        count=curr;
        for(int i=k;i<n;i++)
        {
            if(vowels.find(s[i])!=string :: npos)
            {
                curr++;
            }
            if(vowels.find(s[i-k])!=string :: npos)
            {
                curr--;
            }
            count=max(count,curr);
        }
        return count;

    }
};