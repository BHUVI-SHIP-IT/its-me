class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        vector<vector<int>> result;
        int n = s.size();
        int start = 0;
        
        for (int i = 0; i < n; ++i) {
           
            if (i == n - 1 || s[i] != s[i + 1]) {
                int length = i - start + 1;
                if (length >= 3) {
                    result.push_back({start, i});
                }
                start = i + 1; 
            }
        }
        
        return result;
    }
};
