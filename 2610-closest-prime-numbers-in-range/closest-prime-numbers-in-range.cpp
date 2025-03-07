class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        vector<bool> isPrime(right + 1, true);
        sieve(isPrime, right); // Mark primes using Sieve of Eratosthenes

        vector<int> primesInRange;
        for (int i = max(2, left); i <= right; i++) {
            if (isPrime[i]) {
                primesInRange.push_back(i);
            }
        }

        if (primesInRange.size() < 2) return {-1, -1}; 

        int num1 = -1, num2 = -1, minDiff = INT_MAX;
        for (int i = 0; i < primesInRange.size() - 1; i++) {
            int diff = primesInRange[i + 1] - primesInRange[i];
            if (diff < minDiff) {
                minDiff = diff;
                num1 = primesInRange[i];
                num2 = primesInRange[i + 1];
            }
        }
        return {num1, num2};
    }


    void sieve(vector<bool>& isPrime, int n) {
        isPrime[0] = isPrime[1] = false; 
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
    }
};
