class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> expected;
        expected=heights;
        int count=0;
        sort(heights.begin(),heights.end());
        for(int i=0;i<heights.size();i++){
            if(heights[i]!=expected[i]) count++;
        }
        return count;
    }
};