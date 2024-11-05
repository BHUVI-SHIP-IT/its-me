class Solution:
    def findComplement(self, num: int) -> int:
        numbit=num.bit_length()
        m=(1<<numbit)-1
        return m^num
        