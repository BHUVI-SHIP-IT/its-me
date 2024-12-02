class Solution {
public:
    int numberOfSpecialChars(string word) {
        bool low[26] = {false}, up[26] = {false};

        // Traverse the string and mark corresponding characters
        for (char c : word) {
            if (islower(c)) {
                low[c - 'a'] = true;
            } else if (isupper(c)) {
                up[c - 'A'] = true;
            }
        }

        // Count matching lowercase and uppercase pairs
        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (low[i] && up[i]) {
                count++;
            }
        }

        return count;
    }
};
