/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return \t     -1 if num is higher than the picked number
 *\t\t\t      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int start = 0;
        int end = n;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            int pick = guess(mid);
            if (pick == 0) return mid; // Found the number
            if (pick == -1) end = mid - 1; // Number is lower
            if (pick == 1) start = mid + 1; // Number is higher
        }
        return -1;
    }
};
