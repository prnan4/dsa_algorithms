class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        pos_sign = True
        sign_encountered = False
        digit_encountered = False
        number = ""
        
        for ch in s:
            if ch == "-":
                if (not sign_encountered) and (not digit_encountered):
                    pos_sign = False
                    sign_encountered = True
                else:
                    break
            elif ch == "+":
                if (not sign_encountered) and (not digit_encountered):
                    sign_encountered = True
                    continue
                else:
                    break
            elif ch.isdigit():
                digit_encountered = True
                number += ch
            elif ch == " " and number == "":
                if not sign_encountered:
                    continue
                else:
                    break
            else:
                break
                
        multiplier = 1
        res = 0
        for digit in number[::-1]:
            res += int(digit) * multiplier
            multiplier *= 10
        
        if not pos_sign:
            res *= -1
            
        if res < -2147483648:
            return -2147483648
        if res > 2147483647:
            return 2147483647
        
        return res
            