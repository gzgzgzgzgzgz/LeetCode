import sys
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) == 0:
            return 0
        #see the first position -> three cases + - number
        isNegative = False
        res = 0
        if str[0] == "+" or str[0] == "-" or str[0].isdigit():
            if str[0] == "+" or str[0] == "-":
                p = 0
                while (p < len(str) and not str[p].isdigit() ):
                    p+=1
                if p >= len(str):
                    return 0
                if str[0] == "-":
                    isNegative = True
                if not str[1].isdigit():
                    return 0
            p = 0
            while (not str[p].isdigit()):
                p+=1
            while (p < len(str) and str[p].isdigit()):
                res *= 10
                res += int(str[p])
                if (res >= 2 ** 31):
                    return -2**31 if isNegative else 2**31-1
                p+=1
            return -res if isNegative else res
        else:
            return 0
        