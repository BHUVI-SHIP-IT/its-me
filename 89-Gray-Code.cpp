class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> gray;
        for(int i=0;i<pow(2,n);++i){
            gray.push_back(i^(i>>1));
        }
        return gray;
    }
};