class Solution {
public:
    int minimizedMaximum(int n, vector<int>& quantities) {
        int low=1;
        int high= *max_element(quantities.begin(),quantities.end());
        while(low<high){
            int mid=(low+high)/2;
            int required_stores=0;
            for(int quantity  : quantities){
                required_stores+=(quantity + mid-1)/mid;

            }
            if(required_stores<=n) high=mid;
            else low=mid+1;
        }
        return low;
    }
};