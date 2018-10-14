#coding=utf-8

# //==================================================================
# // 《剑指Offer——名企面试官精讲典型编程题》代码
# // 作者：何海涛
# //==================================================================
#
# // 面试题10：斐波那契数列
# // 题目：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。


class Solution:
    def fibonacci(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]

    def jumpFloor(self, number):
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number+1):
                tempArray[(i+1)%2] = tempArray[0] + tempArray[1]
        return tempArray[(number + 1)%2]

def main():



    s = Solution()

    print (s.fibonacci(100))
    print (s.jumpFloor(3))


if __name__ == '__main__':
    main()