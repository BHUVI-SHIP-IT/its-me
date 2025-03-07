class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        vector<int> optimus_prime;
        
        for (int i = left; i <= right; i++) {
            if (isPrime(i)) {
                optimus_prime.push_back(i);
            }
        }

        if (optimus_prime.size() < 2) return {-1, -1}; 

        int num1 = -1, num2 = -1;
        int min_diff = INT_MAX;

        for (int i = 0; i < optimus_prime.size() - 1; i++) {
            int diff = abs(optimus_prime[i] - optimus_prime[i + 1]);
            if (diff < min_diff) {
                min_diff = diff;
                num1 = optimus_prime[i];
                num2 = optimus_prime[i + 1];
            }
        }
        return {num1, num2};
    }

private:
    bool isPrime(int n) {
        if (n < 2) return false;
        if (n == 2 || n == 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;

        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
};
