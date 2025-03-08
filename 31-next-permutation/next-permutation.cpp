

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int left = n - 2;

        while (left >= 0 && nums[left] >= nums[left + 1]) {
            left--;
        }

        if (left >= 0) {
            int r = n - 1; 
            while (nums[r] <= nums[left]) {
                r--;
            }
            swap(nums[left], nums[r]);
        }

        left = left + 1;
        int r = n - 1; 
        while (left < r) {
            swap(nums[left], nums[r]);
            left++;
            r--;
        }
    }
};


