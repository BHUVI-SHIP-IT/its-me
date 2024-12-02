class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        vector<int> result;
        
        for(int num : nums){
            if(num%2==0){
                result.push_back(num);
            }
        }
        for(int num : nums){
            if(num%2!=0){
                result.push_back(num);
            }
        }
        return result;
    }
};