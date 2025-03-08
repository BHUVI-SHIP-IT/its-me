class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int count_black=0;
        int count_max=0;
        for(int i=0;i<blocks.size();++i)
        {
            if(blocks[i]=='B')
            {
                ++count_black;
            }
            if(i>=k && blocks[i-k]=='B')
            {
                --count_black;
            }
            count_max=max(count_max,count_black);
        }
        return abs(count_max-k);
    }
};