class Solution {
public:
    int minimumChairs(string s) {
        int ecount=0,ans=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='E'){
                ecount++;
                ans=max(ans,ecount);
            }
            else{
                ecount--;
            }
        }
        return ans;
    }
};