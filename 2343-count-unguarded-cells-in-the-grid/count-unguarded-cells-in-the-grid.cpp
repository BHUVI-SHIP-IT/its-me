class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<char>> grid(m, vector<char>(n, 0));
        for (auto& g : guards) grid[g[0]][g[1]] = 'G';
        for (auto& w : walls) grid[w[0]][w[1]] = 'W';

        auto mark = [&](int r, int c, int dr, int dc) {
            while (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] != 'G' && grid[r][c] != 'W') {
                grid[r][c] = 'X';
                r += dr, c += dc;
            }
        };

        for (auto& g : guards) {
            mark(g[0], g[1] + 1, 0, 1);
            mark(g[0], g[1] - 1, 0, -1);
            mark(g[0] + 1, g[1], 1, 0);
            mark(g[0] - 1, g[1], -1, 0);
        }

        int unguarded = 0;
        for (auto& row : grid)
            unguarded += count(row.begin(), row.end(), 0);
        return unguarded;
    }
};
