class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int left=0;
        int right=0;
        int zero=0;
        int maxlen=0;
        while(right<nums.size())
        {
            if(nums[right]==0)
            {
                zero++;
            }
            while(zero>1)
            {
                if(nums[left]==0)
                {
                    zero--;
                }
                left++;
            }
            maxlen=max(maxlen,right-left);
            right++;
        }
        return maxlen;
        
    }
};