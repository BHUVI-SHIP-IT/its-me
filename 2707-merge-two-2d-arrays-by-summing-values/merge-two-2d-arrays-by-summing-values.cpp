class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        map<int,int> merged;
        for(auto& row : nums1)
        {
            merged[row[0]]+=row[1];
        }
        for(auto& row : nums2)
        {
            merged[row[0]]+=row[1];
        }
        vector<vector<int>> res;
        for(auto& entry : merged)
        {
            res.push_back({entry.first,entry.second});
        }
        return res;
    }
};