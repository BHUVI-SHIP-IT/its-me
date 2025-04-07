class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> result;
        if (s.length() < 10) return result; 

        unordered_map<string, int> map;

        for (int i = 0; i <= s.length() - 10; ++i) {
            string substring = s.substr(i, 10);
            if (map.count(substring)) {
                if (map[substring] == 1) {
                    result.push_back(substring);
                }
                map[substring]++;
            } else {
                map[substring] = 1;
            }
        }
        
        return result;
    }
};