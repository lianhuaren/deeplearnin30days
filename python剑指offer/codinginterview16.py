#coding=utf-8



class Solution:

    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1/base


        result = self.Power(base, exponent >> 1)
        print (result)
        result *= result
        if(exponent & 0x1) == 1:
            result *= base
        return result

def main():



    s = Solution()

    print (s.Power(2,-3))

    print (-3 >> 1)


if __name__ == '__main__':
    main()