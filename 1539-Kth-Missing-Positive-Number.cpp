class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int left=0;
        int right=arr.size()-1;
        while(left<=right){
            int mid=left+(right-left)/2;
            int miss=arr[mid]-(mid+1);
            if(miss<k){
                left=left+1;
            }
            else{
                right=right-1;
            }
        }
        return left+k;
    }
};