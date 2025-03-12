class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int post=0;
        int negt=0;

        for(int n : nums)
        {
            if(n>0)
            {
                post++;
            }
            else if(n<0)
            {
                negt++;
            }
        }
        return max(post,negt);
    }
};