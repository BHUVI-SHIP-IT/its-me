class Solution {
public:

    bool check(vector<int>& nums,int k,int cap)
    {
        int n=nums.size();
        int count=0;
        for(int i=0;i<n;i++)
        {
            if(nums[i]<=cap)
            {
                count++;
                i++;
            }
            if(count>=k) return true;
        }
        return false;
    }

    int minCapability(vector<int>& nums, int k) {
        int l=*min_element(nums.begin(),nums.end());
        int r=*max_element(nums.begin(),nums.end());
       int ans=r;
        while(l<=r)
        {
            int mid=l+(r-l)/2;
            if(check(nums,k,mid))
            {
                ans=mid;
                r=mid-1;
            }
            else
            {
                l=mid+1;

            }

        }
        return ans;
    }
};