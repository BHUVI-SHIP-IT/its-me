class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isdivide(num):
            for digit in str(num):
                if digit=='0' or num%int(digit)!=0:
                    return False
            return True
        return[num for num in range(left,right+1) if isdivide(num)]