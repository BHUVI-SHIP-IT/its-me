class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0 || (x%10==0 && x!=0)) return false;
        int reverse=0;
        while(reverse<x){
            reverse=reverse*10+x%10;
            x/=10;
        }
        return x==reverse || x==reverse/10;
    }
};