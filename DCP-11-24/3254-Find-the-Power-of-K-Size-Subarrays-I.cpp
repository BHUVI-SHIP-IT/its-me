#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        vector<int> result;
        for (int i = 0; i <= nums.size() - k; i++) {
            // Extract subarray
            vector<int> subarray(nums.begin() + i, nums.begin() + i + k);

            // Check if sorted and consecutive
            bool isValid = true;
            for (int j = 1; j < k; j++) {
                if (subarray[j] != subarray[j - 1] + 1) {
                    isValid = false;
                    break;
                }
            }

            // Add result based on validity
            if (isValid) {
                result.push_back(*max_element(subarray.begin(), subarray.end()));
            } else {
                result.push_back(-1);
            }
        }
        return result;
    }
};


