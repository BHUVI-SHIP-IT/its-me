class Solution {
public:
    vector<int> fairCandySwap(vector<int>& aliceSizes, vector<int>& bobSizes) {
        int alicesum=0;
        int bobsum=0;
        for(int a : aliceSizes) alicesum+=a;
        for(int b : bobSizes) bobsum+=b;
        int diff=(alicesum-bobsum)/2;
        for(int x : aliceSizes){
            for(int y : bobSizes){
                if(x==y+diff){
                    return {x,y};
                }
            }
        }
        return {};

    }
};