#coding=utf-8

# //==================================================================
# // 《剑指Offer——名企面试官精讲典型编程题》代码
# // 作者：何海涛
# //==================================================================
#
# // 面试题9：用两个栈实现队列
# // 题目：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail
# // 和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


def main():



    s = Solution()
    s.push('a')
    s.push('b')
    s.push('c')


    print (s.pop())
    print (s.pop())
    s.push('d')
    print (s.pop())


if __name__ == '__main__':
    main()