class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10
                total_sum += digit ** 2
                number //= 10
            return total_sum
        
        seen_numbers = set()
        
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = get_next(n)
        
        return n == 1

        