class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int up=1;
        int down=1;
        int n=nums.size();
        if(n<2) return n;
        for(int i=1;i<n;i++)
        {
            if(nums[i]>nums[i-1])
            {
                up=down+1;
            }
            else if(nums[i]<nums[i-1])
            {
                down=up+1;
            }
        }
        return max(up,down);
    }
};