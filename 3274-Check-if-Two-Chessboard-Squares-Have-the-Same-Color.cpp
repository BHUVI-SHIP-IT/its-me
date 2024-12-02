class Solution {
public:
    bool checkTwoChessboards(string coordinate1, string coordinate2) {
        auto isBlack = [](const string& coord) {
            return (coord[0] - 'a' + coord[1] - '1') % 2 == 0;
        };
        return isBlack(coordinate1) == isBlack(coordinate2);
    }
};