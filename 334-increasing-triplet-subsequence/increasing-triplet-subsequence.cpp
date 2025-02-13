class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first=INT_MAX;
        int second=INT_MAX;
        for(int num : nums)
        {
            if(first>=num)
            {
                first=num;
            }
            else if(second>=num)
            {
                second=num;
            }
            else
            {
                return true;
            }
        }
        return false;
    }
};