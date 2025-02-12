class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map<int,int> summap;
        for(int a : nums1)
        {
            for(int b : nums2)
            {
                summap[a+b]++;
            }
        }
        int count =0;
        for(int c : nums3)
        {
            for(int d : nums4)
            {
                int target=-(c+d);
                if(summap.count(target))
                {
                    count+=summap[target];
                }
            }
        }
        return count;
    }
};