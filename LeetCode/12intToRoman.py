#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/9/23 21:20
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        if 1 <= num <= 3:
            result = result + 'I'*num
        elif num == 4:
            result = result + 'IV'
        elif 4 < num <= 8:
            result = result + 'V' + 'I'*(num - 5)
        elif num == 9:
            result = result + 'IX'
        elif 9 < num < 40 and num != 40:
            length_10 = int(num / 10)
            length_5 = int((num - int(num / 10)*10)/5)
            length_1 = num - length_10*10 - length_5*5
            if length_1 == 4 and length_5 != 1:
                result = result + 'X'*length_10 + 'V'*length_5 + 'IV'
            elif length_1 == 4:
                result = result + 'X' * length_10 + 'IX'
            else:
                result = result + 'X' * length_10 + 'V' * length_5 + 'I' * length_1
        elif num == 40:
            result = result + 'XL'
        elif 40 < num < 50:
            length_1 = num - 40
            if length_1 == 9:
                result = result + 'XL' + 'IX'
            elif 5 <= length_1 < 9:
                result = 'XL' + 'V' + 'I'*(length_1-5)
            elif length_1 == 4:
                result = 'XL' + 'IV'
            else:
                result = 'XL' + 'I'*length_1
        elif 50 <= num < 90 and num != 90:
            length_50 = int(num / 50)
            length_10 = int((num - length_50*50)/10)
            length_5 = int((num - length_50*50 - length_10*10)/5)
            length_1 = num - length_50*50 - length_10*10 - length_5*5
            if length_1 == 4 and length_5 != 1:
                result = result + 'L'*length_50 + 'X'*length_10 + 'IV'
            elif length_1 == 4 and length_5 == 1:
                result = result + 'L'*length_50 + 'X'*length_10 + 'IX'
            else:
                result = result + 'L'*length_50 + 'X'*length_10 + 'V'*length_5 + 'I'*length_1
        elif num == 90:
            result = result + 'XC'
        elif 90 < num < 100:
            length_50 = int(num / 50)
            length_10 = int((num - length_50*50)/10)
            length_5 = int((num - length_50*50 - length_10*10)/5)
            length_1 = num - length_50*50 - length_10*10 - length_5*5
            if length_1 == 4 and length_5 != 1:
                result = result + 'XCIV'
            elif length_1 == 4 and length_5 == 1:
                result = result + 'XCIX'
            else:
                result = result + 'XC' + 'V'*length_5 + 'I'*length_1
        elif 100 <= num < 1000 and num != 400 and num != 900:
            length_100 = int(num / 100)
            length_50 = int((num - length_100*100)/50)
            length_10 = int((num - length_100*100 - length_50*50)/10)
            length_5 = int((num - length_100*100 - length_50*50 - length_10*10)/5)
            length_1 = num - length_100*100 - length_50*50 - length_10*10 - length_5*5
            if 400 <= num <= 499:
                result = result + 'CD'
            elif 500 <= num <= 599:
                result = result + 'D'
            elif 600 <= num <= 699:
                result = result + 'DC'
            elif 700 <= num <= 799:
                result = result + 'DCC'
            elif 800 <= num <= 899:
                result = result + 'DCCC'
            elif 900 <= num <= 999:
                result = result + 'CM'
            else:
                result = result + 'C'*length_100

            if length_50 == 1 and length_10 != 4:
                result = result + 'L'
            elif length_50 == 1 and length_10 == 4:
                result = result + 'XC'
            elif length_50 == 0:
                result = result + ''

            if length_10 == 4 and length_50 != 1:
                result = result + 'XL'
            elif length_10 != 4:
                result = result + 'X'*length_10

            if length_5 == 1 and length_1 == 0:
                result = result + 'V'
            elif length_5 == 0 and length_1 == 4:
                result = result + 'IV'
            elif length_5 == 1 and length_1 == 4:
                result = result + 'IX'
            else:
                result = result + 'V'*length_5 + 'I' * length_1
        elif num == 400:
            result = result + 'CD'
        elif num == 900:
            result = result + 'CM'
        elif 1000 <= num <= 3999:
            length_1000 = int(num / 1000)
            length_100 = int((num - length_1000*1000)/100)
            length_50 = int((num - length_1000*1000 - length_100*100)/50)
            length_10 = int((num - length_1000*1000 - length_100 * 100 - length_50*50) / 10)
            length_5 = int((num - length_1000*1000 - length_100 * 100 - length_50*50 - length_10 * 10) / 5)
            length_1 = num - length_1000*1000 - length_100 * 100 - length_50*50 - length_10 * 10 - length_5 * 5
            if length_100 == 4:
                result = result + 'M'*length_1000 + 'CD'
            elif length_100 == 5:
                result = result + 'M'*length_1000 + 'D'
            elif length_100 == 6:
                result = result + 'M' * length_1000 + 'DC'
            elif length_100 == 7:
                result = result + 'M' * length_1000 + 'DCC'
            elif length_100 == 8:
                result = result + 'M' * length_1000 + 'DCCC'
            elif length_100 == 9:
                result = result + 'M'*length_1000 + 'CM'
            else:
                result = result + 'M'*length_1000 + 'C'*length_100

            if length_50 == 1 and length_10 != 4:
                result = result + 'L'
            elif length_50 == 1 and length_10 == 4:
                result = result + 'XC'
            elif length_50 == 0:
                result = result + ''

            if length_10 == 4 and length_50 != 1:
                result = result + 'XL'
            elif length_10 != 4:
                result = result + 'X' * length_10

            if length_5 == 1 and length_1 == 0:
                result = result + 'V'
            elif length_5 == 0 and length_1 == 4:
                result = result + 'IV'
            elif length_5 == 1 and length_1 == 4:
                result = result + 'IX'
            else:
                result = result + 'V' * length_5 + 'I' * length_1
        return result


a = Solution()
print(a.intToRoman(3999))
