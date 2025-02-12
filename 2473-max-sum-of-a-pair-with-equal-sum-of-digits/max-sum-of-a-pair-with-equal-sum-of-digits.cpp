class Solution {
public:
    int maximumSum(vector<int>& nums) {
        unordered_map<int , int>dsm;
        int maxsum=-1;
        for(int num : nums)
        {
            int sum=0;
            int temp=num;
            while(temp>0)
            {
                sum+=temp%10;
                temp/=10;
            }
            if(dsm.count(sum))
            {
                maxsum=max(maxsum,num+dsm[sum]);
            }
            dsm[sum]=max(num,dsm[sum]);
        }
        return maxsum;
    }
    
};