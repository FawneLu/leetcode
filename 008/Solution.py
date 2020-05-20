class Solution:
    def myAtoi(self, str: str) -> int:
        str=str.strip()
        if not str:
            return 0
        res,flag=0,1
        if str[0]=="+":
            str=str[1:]
        elif str[0]=="-":
            str=str[1:]
            flag=-1
        for c in str:
            if c.isdigit():
                res=10*res+ord(c)-ord('0')
            else:
                break
        
        res=flag*res
        res = res if res <=2147483647 else 2147483647
        res = res if res >= -2147483648 else -2147483648
        return res