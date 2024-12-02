class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int largest=-1,second=-1,index=-1;
        for(int i=0;i<nums.size();i++){
            if(nums[i]>largest){
                second=largest;
                largest=nums[i];
                index=i;
            }
            else if(nums[i]>second){
                second=nums[i];
            }
        }
        if(largest>=2*second){
            return index;
        }
        return -1;
    }
};