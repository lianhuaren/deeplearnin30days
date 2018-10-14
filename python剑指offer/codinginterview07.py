#coding=utf-8

# //==================================================================
# // 《剑指Offer——名企面试官精讲典型编程题》代码
# // 作者：何海涛
# //==================================================================
#
# // 面试题7：重建二叉树
# // 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输
# // 入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,
# // 2, 4, 7, 3, 5, 6, 8}和中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}，则重建出
# // 图2.6所示的二叉树并输出它的头结点。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return None
        root = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None
        i = tin.index(pre[0])
        # print (i)
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root


def main():


    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]

    ret = Solution().reConstructBinaryTree(pre, tin)
    out = (ret)
    print (out)

    i = 3
    print (pre[1:i+1], pre[i+1:])
    print (tin[:i], tin[i+1:])

if __name__ == '__main__':
    main()