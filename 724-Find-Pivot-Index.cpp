class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int leftsum=0;
        int totalsum=0;
        for(int num : nums){
            totalsum+=num;
        }
        for(int i=0;i<nums.size();i++){
            if(leftsum==totalsum-leftsum-nums[i]){
                return i;
            }
            leftsum+=nums[i];

        }
        return -1;
    }
};