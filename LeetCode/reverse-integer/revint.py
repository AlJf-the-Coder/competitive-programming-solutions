class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        opp_zeroes = 1
        while x // opp_zeroes > 0:
            opp_zeroes *= 10
        rev = 0
        zeroes = 1
        while True:
            digit = (x % zeroes) // zeroes
            rev += opp_zeroes * digit
            opp_zeroes //= 10
            zeroes *= 10


        
