#coding=utf-8



class Solution:

    def NumberOf1(self, n):
        if n < 0:
            n = n&0xffffffff
        n = bin (n)
        print (n)
        length = len(str(n))
        # print (length)
        count = 0

        for i in range(length):
            print (str(n)[i])
            if "1" == str(n)[i]:
                count += 1
        return count

    def NumberOf2(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n-1)&n
        return count

def main():



    s = Solution()

    # print (s.NumberOf1(9))
    print (s.NumberOf2(9))


if __name__ == '__main__':
    main()