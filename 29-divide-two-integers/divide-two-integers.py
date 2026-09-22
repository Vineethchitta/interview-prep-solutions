class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0:
            return 0
        q = 0
        inc = divisor
        if dividend<0 and divisor<0:
            if divisor == -1:
                dividend = dividend - dividend - dividend
                if dividend>=2147483648:
                    return dividend-1
                return dividend
            while dividend<=divisor:
                temp = divisor
                multiple = 1
                while dividend<=(temp<<1):
                    temp<<=1
                    multiple<<=1
                q+=multiple
                dividend-=temp
        elif dividend>0 and divisor>0:
            if divisor==1:
                return dividend
            while dividend>=divisor:
                temp = divisor
                multiple = 1
                while dividend>=(temp<<1):
                    temp<<=1
                    multiple<<=1
                q+=multiple
                dividend-=temp
        else:
            if divisor==-1:
                return dividend - dividend - dividend
            elif divisor==1:
                return dividend
            if dividend<0:
                dividend = dividend - dividend - dividend
            elif divisor<0:
                divisor = divisor - divisor - divisor
            while dividend>=divisor:
                temp = divisor
                multiple = 1
                while dividend>=(temp<<1):
                    temp<<=1
                    multiple<<=1
                q-=multiple
                dividend-=temp
        return q