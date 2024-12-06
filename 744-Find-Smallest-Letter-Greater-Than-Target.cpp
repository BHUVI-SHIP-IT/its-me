class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int left=0;
        int right=letters.size()-1;
        while(left<=right){
            int mid=left+(right-left)/2;
            
             if(letters[mid]>target){
                right=right-1;
            }
            else{
                left=left+1;
            }
            
        }
        return letters[left%letters.size()];
    }
};