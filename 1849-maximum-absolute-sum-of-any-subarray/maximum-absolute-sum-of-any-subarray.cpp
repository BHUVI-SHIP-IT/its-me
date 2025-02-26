class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int ans=0;
        int max_sum=0;
        int min_sum=0;
        for(int num : nums)
        {
            max_sum=max(num,max_sum+num);
            min_sum=min(num,min_sum+num);
            ans=max({ans,abs(max_sum),abs(min_sum)});
        }
        return ans;
    }
};