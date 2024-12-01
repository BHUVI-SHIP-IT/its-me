class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> major;
        unordered_map<int,int>map;
        int n=nums.size();
        for(int i:nums)
        {
            map[i]++;
        }
        for(const auto& pair : map)
        {
            if(pair.second>n/3){
                major.push_back(pair.first);
            }
        }
        return major;

    }
};